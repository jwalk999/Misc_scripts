import pandas as pd
import requests

BASE_URL = "https://ccmc.gsfc.nasa.gov/DONKI-API/get"


# Coronal Mass Ejection Analysis
def get_cme_analysis(endpoint, start_date, end_date, **extra):
    params_cme_analysis = {"startDate": start_date, "endDate": end_date, **extra}
    cme_r = requests.get(f"{BASE_URL}/{endpoint}", params=params_cme_analysis, timeout=30)
    cme_r.raise_for_status()
    return cme_r.json() if cme_r.text.strip() else []

cme_storms = get_cme_analysis("CMEAnalysis", "2026-10-16", "2026-10-19",
                   catalog="ALL", mostAccurateOnly="true")

def export_cme_analysis():
    # Each dict becomes a row; keys become columns
    cme_df = pd.DataFrame(cme_storms)

    if cme_df.empty:
        print("No CME analyses found for that date range.")
    else:
        # Keep and rename the columns you care about
        cme_columns = {
            "time21_5": "Date/Time",
            "type": "Type",
            "speed": "Speed (km/s)",
            "halfAngle": "Half Angle",
            "latitude": "Latitude",
            "longitude": "Longitude",
            "note": "Note",
        }
        df = cme_df[[c for c in cme_columns if c in cme_df.columns]].rename(columns=cme_columns)
        df["Date/Time"] = pd.to_datetime(
            df["Date/Time"],
            unit="s",
            utc=True
        )
        # Export to CSV file
        df.to_csv("C:/Users/rrebe/Documents/Python Projects/NASA/cme.csv", mode="w", index=False, encoding="utf-8")
export_cme_analysis()



# Solar event notifications
def get_notifications(endpoint, start_date, end_date, description_type):
    params_notifications = {"startDate": start_date, "endDate": end_date, "type": description_type}
    notif_r = requests.get(f"{BASE_URL}/{endpoint}", params=params_notifications, timeout=30)
    notif_r.raise_for_status()
    return notif_r.json() if notif_r.text.strip() else []
notifications = get_notifications("notifications", "2026-10-16", "2026-10-19", "all")

def export_notifications():
    notif_df = pd.DataFrame(notifications)
    if notif_df.empty:
        print("No Notifications found for that date range.")
    else:
        notif_columns = {
            "messageIssueTime": "Issue Time",
            "messageType": "Type",
            "messageBody": "Body"
        }
        df = notif_df[[c for c in notif_columns if c in notif_df.columns]]
        df.to_csv("C:/Users/rrebe/Documents/Python Projects/NASA/notifications.csv", mode="w", index=False, encoding="utf-8")
export_notifications()

