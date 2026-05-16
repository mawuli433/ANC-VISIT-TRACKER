# ANC Visit Tracker — Ghana Edition

**A Python-based Clinical Decision Support Tool for Antenatal Care**
Built for health professionals at the clinic and hospital level in Ghana.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Why This Tool Was Built](#why-this-tool-was-built)
3. [Features](#features)
4. [Clinical Protocols Used](#clinical-protocols-used)
5. [How to Install and Run](#how-to-install-and-run)
6. [How to Use the Tool](#how-to-use-the-tool)
7. [Sample Session](#sample-session)
8. [Danger Signs Reference](#danger-signs-reference)
9. [Risk Factors Reference](#risk-factors-reference)
10. [Limitations and Disclaimer](#limitations-and-disclaimer)
11. [Author](#author)

---

## Project Overview

The **ANC Visit Tracker** is a terminal-based Python application designed to support nurses and midwives in conducting structured antenatal care (ANC) assessments. It automates gestational age calculation, generates a recommended visit schedule, detects missed contacts, screens for danger signs, and flags obstetric risk factors — all in a simple, step-by-step interface that requires no internet connection.

---

## Why This Tool Was Built

Ghana continues to face challenges with antenatal care attendance and early detection of high-risk pregnancies, particularly at the district and community level. According to the Ghana Demographic and Health Survey (GDHS), while ANC attendance rates have improved, the quality and consistency of visits — including timely screening for danger signs — remain gaps in many facilities.

This tool was built to:

- Reduce human error in gestational age calculation
- Ensure no recommended ANC contact is overlooked
- Standardise danger sign and risk factor screening at every visit
- Support nurses working in facilities where doctor availability may be limited

---

## Features

| Feature | Description |
|---|---|
| Gestational Age Calculator | Calculates weeks and days pregnant from the Last Menstrual Period (LMP) |
| EDD Calculator | Estimates Expected Date of Delivery using Naegele's Rule |
| Trimester Classifier | Automatically identifies the patient's current trimester |
| WHO 8-Contact Schedule | Generates a full recommended visit schedule with calendar dates |
| Missed Visit Detector | Compares completed visits against the recommended schedule and flags gaps |
| Danger Signs Screening | 10-item checklist based on Ghana Health Service ANC protocol |
| Risk Factor Screening | 10-item obstetric and medical risk factor checklist |
| Referral Recommendations | Generates clear action steps based on screening results |
| Patient Summary | Prints a structured end-of-session summary for each patient |

---

## Clinical Protocols Used

This tool was developed in alignment with the following clinical guidelines:

- **WHO ANC Model (2016):** Recommends a minimum of 8 contacts during pregnancy at weeks 8, 12, 16, 20, 26, 30, 34, and 36+
- **Ghana Health Service ANC Protocol:** Danger signs checklist and high-risk pregnancy criteria
- **Naegele's Rule:** Standard formula for calculating Expected Date of Delivery (LMP + 280 days)

---

## How to Install and Run

### Requirements

- Python 3.x installed on your computer
- No additional libraries needed — the tool only uses Python's built-in `datetime` module

### Step 1 — Check Python is installed

Open your terminal or command prompt and type:

```
python --version
```

You should see something like `Python 3.11.0`. If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### Step 2 — Download the file

Save `ANC_Visit_Tracker.py` to a folder on your computer, for example your Desktop.

### Step 3 — Run the program

Open your terminal, navigate to the folder where you saved the file, and type:

```
python ANC_Visit_Tracker.py
```

Press Enter. The program will start immediately.

### Running on Mobile (No Laptop)

If you do not have a laptop, you can run this tool for free using [Replit](https://replit.com):

1. Create a free account at replit.com
2. Click **Create Repl** and choose **Python**
3. Copy and paste the full code into the editor
4. Click **Run**

---

## How to Use the Tool

The tool walks you through each assessment step by step. Here is what it will ask you:

**Patient Details**
- Full name, patient ID or folder number, and age

**Last Menstrual Period (LMP)**
- Enter the date in DD/MM/YYYY format
- The tool will automatically calculate gestational age, trimester, and EDD

**Completed ANC Visits**
- Enter how many visits the patient has already attended
- Enter the date of each visit
- The tool will flag any missed contacts

**Danger Signs Screening**
- Answer yes (y) or no (n) for each of the 10 danger signs

**Risk Factor Screening**
- Answer yes (y) or no (n) for each of the 10 risk factors

**Results**
- The tool prints a clinical recommendation and patient summary
- You will be shown the date of the next recommended contact

---

## Sample Session

```
=================================================
     ANC VISIT TRACKER — Ghana Edition
  For Clinic and Hospital Use by Nurses
=================================================

NEW PATIENT ASSESSMENT

Patient Full Name       : Abena Mensah
Patient ID / Folder No. : GH-2024-0045
Patient Age (years)     : 24

Enter Last Menstrual Period (LMP) (DD/MM/YYYY): 10/09/2025

   Gestational Age : 27 weeks and 3 days
   Trimester       : Second Trimester (14–27 weeks)
   Expected Date of Delivery (EDD): 17 June 2026

Recommended Contact Schedule:
   Week  8 — 05 Nov 2025  [Should have occurred]
   Week 12 — 03 Dec 2025  [Should have occurred]
   Week 16 — 31 Dec 2025  [Should have occurred]
   Week 20 — 28 Jan 2026  [Should have occurred]
   Week 26 — 11 Mar 2026  [Should have occurred]
   Week 30 — 08 Apr 2026  [Due]
   Week 34 — 06 May 2026  [Due]
   Week 36 — 20 May 2026  [Due]

How many ANC visits has this patient completed so far? 3
Enter date of Visit 1 (DD/MM/YYYY): 08/11/2025
Enter date of Visit 2 (DD/MM/YYYY): 05/12/2025
Enter date of Visit 3 (DD/MM/YYYY): 30/01/2026

⚠️  MISSED CONTACTS DETECTED (2):
   • Week 16 contact — was due around 31 Dec 2025
   • Week 26 contact — was due around 11 Mar 2026

   ACTION: Counsel patient on importance of ANC visits.
   Schedule catch-up appointment as soon as possible.
```

---

## Danger Signs Reference

The tool screens for the following 10 danger signs at every assessment:

1. Severe headache or blurred vision
2. Facial or hand swelling (oedema)
3. Vaginal bleeding
4. Severe abdominal pain
5. Fever (temperature above 38°C)
6. Reduced or absent fetal movement
7. Difficulty breathing
8. Convulsions or loss of consciousness
9. Foul-smelling vaginal discharge
10. Severe vomiting (unable to keep food down)

**If any danger sign is present:** The tool recommends immediate referral to a doctor or emergency obstetric unit.

---

## Risk Factors Reference

The tool screens for the following 10 obstetric and medical risk factors:

1. Age below 18 or above 35
2. Grand multiparity (4 or more previous pregnancies)
3. Previous caesarean section
4. Previous stillbirth or neonatal death
5. Multiple pregnancy (twins or more)
6. Known hypertension or diabetes
7. Known HIV positive status
8. Anaemia (pallor, fatigue, Hb below 11 g/dL)
9. Malaria in this pregnancy
10. Less than 2 years since last delivery

**If any risk factor is present:** The tool flags the patient as high risk and recommends doctor review.

---

## Limitations and Disclaimer

This tool is intended as a **clinical decision support aid only**. It does not replace clinical judgment, physical examination, or doctor review.

- The tool does not store patient data between sessions
- It does not connect to any hospital information system
- EDD calculation assumes a regular 28-day menstrual cycle (Naegele's Rule)
- Gestational age based on LMP may differ from ultrasound dating
- All clinical decisions must be confirmed by a qualified healthcare professional

This tool was built for educational and practical support purposes in the context of nursing training and community health practice in Ghana.

---

## Author

Built by Mr. Suleman, on community health placement in Nkoranza, Bono East Region, Ghana.
Developed as part of NUS 358: Research Methods coursework and digital skills training.

Clinical protocols referenced from:
- World Health Organization (2016). *WHO recommendations on antenatal care for a positive pregnancy experience.* Geneva: WHO.
- Ghana Health Service. *Antenatal Care Protocol.* Accra: GHS.
