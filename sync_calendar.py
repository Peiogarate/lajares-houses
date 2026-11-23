"""
Sincroniza la disponibilidad de las casas desde sus calendarios iCal
(Airbnb -> Google Calendar, o directamente el enlace iCal de Airbnb)
y escribe data/availability.js, que la web lee al cargar.

Uso:  python sync_calendar.py
No necesita librerias externas. Lo ejecuta automaticamente la
GitHub Action de .github/workflows/sync-calendar.yml cada 3 horas.
"""
import json
import re
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# Pega aqui el enlace iCal de cada casa. Sirve tanto el de Airbnb
# (Anuncio > Disponibilidad > Sincronizar calendarios > Exportar calendario)
# como el de Google Calendar publico que ya usa la web antigua.
CALENDARS = {
    "mali": [
        "https://calendar.google.com/calendar/ical/4q3s4fajef8ef0o060i5bh5mqb7ihmcp%40import.calendar.google.com/public/basic.ics",
    ],
    "dudi": [
        "https://calendar.google.com/calendar/ical/mj0j5lct1ub0f2rckjivn5cvmsi9gnsu%40import.calendar.google.com/public/basic.ics",
    ],
}

OUT = Path(__file__).parent / "data" / "availability.js"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "calendar-sync/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def parse_date(value: str) -> date:
    value = value.strip()
    return datetime.strptime(value[:8], "%Y%m%d").date()


def parse_ics(text: str):
    # Unfold folded lines (RFC 5545)
    text = re.sub(r"\r?\n[ \t]", "", text)
    ranges = []
    for block in text.split("BEGIN:VEVENT")[1:]:
        start = end = None
        for line in block.splitlines():
            key, _, val = line.partition(":")
            name = key.split(";")[0].upper()
            if name == "DTSTART":
                start = parse_date(val)
            elif name == "DTEND":
                end = parse_date(val)
        if start:
            end = end or start + timedelta(days=1)
            ranges.append((start, end))  # end = checkout day (free for a new check-in)
    return ranges


def merge(ranges):
    out = []
    for s, e in sorted(ranges):
        if out and s <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], e))
        else:
            out.append((s, e))
    return out


def main():
    today = date.today()
    data = {"updated": datetime.now(timezone.utc).isoformat(timespec="minutes"), "houses": {}}
    for house, urls in CALENDARS.items():
        ranges = []
        for url in urls:
            try:
                ranges += parse_ics(fetch(url))
            except Exception as exc:  # keep the rest working if one feed fails
                print(f"[aviso] {house}: no se pudo leer {url[:60]}... ({exc})")
        ranges = [(s, e) for s, e in merge(ranges) if e >= today]
        data["houses"][house] = [[s.isoformat(), e.isoformat()] for s, e in ranges]
        print(f"{house}: {len(ranges)} bloques ocupados")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(
        "// Generado por sync_calendar.py - no editar a mano\n"
        "window.AVAILABILITY = " + json.dumps(data, indent=1) + ";\n",
        encoding="utf-8",
    )
    print("Escrito", OUT)


if __name__ == "__main__":
    main()
