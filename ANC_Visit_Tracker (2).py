# ============================================================
# ANC VISIT TRACKER - Ghana Clinic/Hospital Edition
# Built for use by nurses and midwives at the facility level
# Based on Ghana Health Service ANC Protocol (4+ visits min)
# and WHO ANC Model (8 contacts recommended)
# ============================================================

from datetime import datetime, timedelta

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_date(prompt):
    """Collect and validate a date input from the user."""
    while True:
        date_str = input(prompt + " (DD/MM/YYYY): ")
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            print("   ❌ Invalid date format. Please use DD/MM/YYYY.")


def calculate_gestational_age(lmp):
    """Calculate gestational age in weeks from Last Menstrual Period."""
    today = datetime.today()
    days_pregnant = (today - lmp).days
    weeks = days_pregnant // 7
    days = days_pregnant % 7
    return weeks, days


def calculate_edd(lmp):
    """Calculate Expected Date of Delivery using Naegele's Rule."""
    edd = lmp + timedelta(days=280)
    return edd


def get_trimester(weeks):
    """Return trimester based on gestational age in weeks."""
    if weeks < 14:
        return "First Trimester (0–13 weeks)"
    elif 14 <= weeks <= 27:
        return "Second Trimester (14–27 weeks)"
    else:
        return "Third Trimester (28+ weeks)"


def anc_visit_schedule(lmp):
    """
    Generate recommended ANC visit schedule based on WHO 8-contact model.
    Contacts: 8, 12, 16, 20, 26, 30, 34, 36+ weeks
    """
    contact_weeks = [8, 12, 16, 20, 26, 30, 34, 36]
    schedule = []
    for week in contact_weeks:
        visit_date = lmp + timedelta(weeks=week)
        schedule.append((week, visit_date))
    return schedule


def check_missed_visits(schedule, visits_done):
    """
    Compare recommended schedule against completed visits.
    Flag any contacts that should have happened but were missed.
    """
    today = datetime.today()
    missed = []
    for week, date in schedule:
        if date < today:  # Visit should have already happened
            # Check if any completed visit falls within 2 weeks of scheduled date
            covered = any(
                abs((v - date).days) <= 14 for v in visits_done
            )
            if not covered:
                missed.append((week, date))
    return missed


def flag_danger_signs():
    """
    Walk the nurse through a danger signs checklist.
    Based on Ghana Health Service ANC danger signs protocol.
    """
    print("\n" + "=" * 50)
    print("   DANGER SIGNS SCREENING")
    print("=" * 50)
    print("Answer yes (y) or no (n) for each sign:\n")

    danger_signs = {
        "Severe headache or blurred vision"         : False,
        "Facial or hand swelling (oedema)"          : False,
        "Vaginal bleeding"                          : False,
        "Severe abdominal pain"                     : False,
        "Fever (temperature > 38°C)"                : False,
        "Reduced or absent fetal movement"          : False,
        "Difficulty breathing"                      : False,
        "Convulsions or loss of consciousness"      : False,
        "Foul-smelling vaginal discharge"           : False,
        "Severe vomiting (unable to keep food down)": False,
    }

    flags = []

    for sign, _ in danger_signs.items():
        answer = input(f"   {sign}? (y/n): ").strip().lower()
        if answer == "y":
            flags.append(sign)

    return flags


def flag_risk_factors():
    """
    Screen for obstetric and medical risk factors.
    Based on Ghana Health Service high-risk pregnancy criteria.
    """
    print("\n" + "=" * 50)
    print("   RISK FACTOR SCREENING")
    print("=" * 50)
    print("Answer yes (y) or no (n) for each:\n")

    risk_factors = [
        "Age below 18 or above 35",
        "Grand multiparity (4 or more previous pregnancies)",
        "Previous caesarean section",
        "Previous stillbirth or neonatal death",
        "Multiple pregnancy (twins or more)",
        "Known hypertension or diabetes",
        "Known HIV positive status",
        "Anaemia (pallor, fatigue, Hb < 11 g/dL)",
        "Malaria in this pregnancy",
        "Less than 2 years since last delivery",
    ]

    flags = []

    for factor in risk_factors:
        answer = input(f"   {factor}? (y/n): ").strip().lower()
        if answer == "y":
            flags.append(factor)

    return flags


def print_referral_advice(danger_flags, risk_flags):
    """
    Generate referral and management advice based on flagged items.
    """
    print("\n" + "=" * 50)
    print("   CLINICAL SUMMARY & RECOMMENDATIONS")
    print("=" * 50)

    if danger_flags:
        print("\n🚨  DANGER SIGNS DETECTED:")
        for sign in danger_flags:
            print(f"     • {sign}")
        print("\n   ⚠️  ACTION: This patient requires IMMEDIATE referral")
        print("   to a doctor or emergency obstetric unit.")
        print("   Do NOT send this patient home unreviewed.")

    elif risk_flags:
        print("\n⚠️  RISK FACTORS IDENTIFIED:")
        for risk in risk_flags:
            print(f"     • {risk}")
        print("\n   ACTION: Flag this patient as HIGH RISK.")
        print("   Ensure doctor review at next visit.")
        print("   Increase monitoring frequency.")

    else:
        print("\n✅  No danger signs or major risk factors detected.")
        print("   ACTION: Continue routine ANC monitoring.")
        print("   Reinforce appointment adherence and nutrition.")


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 50)
print("     ANC VISIT TRACKER — Ghana Edition")
print("  For Clinic and Hospital Use by Nurses")
print("=" * 50)

while True:

    print("\n" + "=" * 50)
    print("   NEW PATIENT ASSESSMENT")
    print("=" * 50)

    # --- PATIENT DETAILS ---
    name    = input("\nPatient Full Name       : ")
    id_num  = input("Patient ID / Folder No. : ")
    age     = int(input("Patient Age (years)     : "))

    # --- LMP & GESTATIONAL AGE ---
    print("\n--- GESTATIONAL AGE CALCULATION ---")
    lmp = get_date("Enter Last Menstrual Period (LMP)")

    weeks, days = calculate_gestational_age(lmp)
    edd         = calculate_edd(lmp)
    trimester   = get_trimester(weeks)

    print(f"\n   Gestational Age : {weeks} weeks and {days} days")
    print(f"   Trimester       : {trimester}")
    print(f"   Expected Date of Delivery (EDD): {edd.strftime('%d %B %Y')}")

    # --- VALIDITY CHECK: LMP must be within last 42 weeks ---
    if weeks > 42:
        print("\n   ❌ LMP entered suggests pregnancy over 42 weeks.")
        print("   Please verify the LMP date with the patient.")

    # --- ANC VISIT SCHEDULE ---
    print("\n--- ANC VISIT SCHEDULE (WHO 8-Contact Model) ---")
    schedule = anc_visit_schedule(lmp)

    print("\n   Recommended Contact Schedule:")
    today = datetime.today()
    for week, date in schedule:
        status = "✅ Due" if date > today else "📅 Should have occurred"
        print(f"   Week {week:>2} — {date.strftime('%d %b %Y')}  [{status}]")

    # --- COMPLETED VISITS ---
    print("\n--- COMPLETED ANC VISITS ---")
    visits_done = []
    num_visits  = int(input("How many ANC visits has this patient completed so far? "))

    for i in range(num_visits):
        v_date = get_date(f"Enter date of Visit {i + 1}")
        visits_done.append(v_date)

    # --- MISSED VISITS ---
    missed = check_missed_visits(schedule, visits_done)

    if missed:
        print(f"\n⚠️  MISSED CONTACTS DETECTED ({len(missed)}):")
        for week, date in missed:
            print(f"   • Week {week} contact — was due around {date.strftime('%d %b %Y')}")
        print("\n   ACTION: Counsel patient on importance of ANC visits.")
        print("   Schedule catch-up appointment as soon as possible.")
    else:
        print("\n✅  No missed contacts detected. Patient is on schedule.")

    # --- DANGER SIGNS ---
    danger_flags = flag_danger_signs()

    # --- RISK FACTORS ---
    risk_flags = flag_risk_factors()

    # --- RECOMMENDATIONS ---
    print_referral_advice(danger_flags, risk_flags)

    # --- NEXT VISIT ---
    print("\n--- NEXT RECOMMENDED VISIT ---")
    upcoming = [(w, d) for w, d in schedule if d > today]
    if upcoming:
        next_week, next_date = upcoming[0]
        print(f"   Next ANC contact due at Week {next_week}")
        print(f"   Recommended date: {next_date.strftime('%d %B %Y')}")
    else:
        print("   Patient is at or beyond Week 36.")
        print("   Weekly monitoring recommended until delivery.")

    # --- SUMMARY FOOTER ---
    print("\n" + "=" * 50)
    print(f"   Patient  : {name}  |  ID: {id_num}  |  Age: {age}")
    print(f"   GA       : {weeks} weeks {days} days  |  EDD: {edd.strftime('%d %b %Y')}")
    print(f"   Visits   : {num_visits} completed  |  Missed: {len(missed)}")
    print(f"   Danger   : {'YES ⚠️' if danger_flags else 'None ✅'}")
    print(f"   Risk     : {'YES ⚠️' if risk_flags else 'None ✅'}")
    print("=" * 50)

    # --- CONTINUE OR EXIT ---
    choice = input("\nAssess another patient? (yes/no): ")
    if choice.strip().lower() == "no":
        print("\nSession ended. All the best in your practice. 👋")
        break
