# {{ league_name }}: Umpire Coordinator (UIC) Handbook
*A Veteran's Playbook for Program Excellence*

---

# 1. UIC Philosophy: The Veteran's Perspective

As a veteran UIC your role is not just "scheduling." You are the guardian of the game's integrity and the protector of the youth who step onto the turf in blue.

## The "Shield" Mentality
Your primary responsibility is to be the shield between the umpires (especially youth umpires) and external pressures from coaches or administrative bodies.
- Emotional responses from the field or policy friction from above should not reach the youth umpires.
- You must be the one person who says: "The umpire's decision is final, and any breach of sportsmanship directed at our youth umpires is a non-starter."

## Training is Recruitment
You don't "hire" umpires; you build them.
- A youth umpire who feels supported after a tough call will come back. A youth umpire who feels abandoned by their leadership will quit.

---

# 2. Platform Mastery: Platform-Specific Guides

[[ IF assignment_tool == 'RefTown' ]]
## RefTown Mastery: Season Setup & Management

### Registration & Onboarding
- **The Global Link:** [www.reftown.com](http://www.reftown.com) -> Register -> Official.
- **The Direct League Link:** [registration.asp?RID=1&RegType=Official&Assoc={{ league_id }}](https://reftown.com/registration.asp?RID=1&RegType=Official&Assoc={{ league_id }})
- **Resilience Navigation:** If the direct link breaks, go to the RefTown Home Page -> **Register** -> Select **Official** -> Search for **{{ league_name }} ({{ league_id }})**.
- **Admin Management:** Once logged in as an admin, go to **Other -> Interactive forms** to manage the specific fields on this form.
- **The Onboarding Loop (The "Pain Point"):** RefTown's registration form captures basic data, but it does **not** allow for the direct upload or validation of compliance data (Background Checks/Concussion Training) during the initial sign-up. 
- **The Official Onboarding Workflow:**
    1. **Initial Screening:** When a new registration appears in the pending queue, check the age.
    2. **Safety Officer Coordination (Adults Only):** If the applicant is an adult (18+), you **must** notify the League Safety Officer. Do not approve the registration until the Safety Officer confirms the background check is cleared.
    3. **Approval:** Once cleared by the Safety Officer, approve the registration.
    4. **The Directory Pivot:** Navigate to the **Directory** in the main menu to finalize the profile.
    5. **The Search:** Find the newly approved umpire.
    6. **The Edit:** Click on the umpire's name to open their full profile.
    7. **Additional Info:** Navigate to the **"Additional Info"** section to record:
        - **Background Check Status:** Mark as cleared once confirmed by the Safety Officer.
        - **Concussion Training Completion:** Verify annually.
        - **Official Positions:** Use the **'P'** tag for Plate-qualified officials.
- **Support Resources:** Visit the [RefTown Home Page](https://www.reftown.com/) and navigate to the **Support** section (or visit the [Direct Support Center](https://reftown.com/kbp/index.php)) for advanced form configuration and "Interactive Form" archiving.

### Handling Inquiries & Recruitment
You will receive automated emails from **RefTown Feedback** (Subject: "Umpiring little league"). These are high-value leads, often former players from your local high schools.

- **The "High-Value" Lead:** Former players are your best recruits. They know the fields, the culture, and the game.
- **Response Template:**
  > "Hello [Name], thanks for reaching out! It's great to hear you played at {{ league_abbreviation }}. We'd love to have you back in blue. To get started, please register here: {{ registration_link }}. Once you've signed up, I'll send you the info for the next training session and how to self-assign games. Welcome back!"
- **The Follow-up:** Don't just send the link. Mention the competitive pay rates—for a high schooler, this is the best hourly wage they can find.

### Assignment Lifecycle & Communication
Once the schedule is live, the "Second Season" begins: the hunt for coverage.

1. **The Request:** Umpires browse the schedule and "Request" games. They are not yet assigned; the game appears as "Requested" in the pool.
2. **The Assignment:** The UIC reviews requests and assigns the umpire. 
   - **UIC Tip:** Prioritize youth umpires for lower-division games to build their confidence.
3. **The Confirmation:** Once the UIC assigns the umpire, RefTown sends an automated notification to the **Coach**. This is the coach's signal that their game is covered.

### The "No Self-Unassign" Protocol
This is a critical policy for maintaining schedule integrity.
- **The Rule:** Once an umpire is assigned to a game, they **cannot** un-assign themselves in RefTown.
- **The Process:** The umpire must contact the UIC directly via email/text to request a drop.
- **The Rationale:** This prevents "Silent Gaps." When an umpire contacts you to drop, it triggers the UIC to immediately blast the pool for coverage. If they could drop silently, a game might go uncovered without the UIC ever knowing.

### Umpire Grading & Coach Feedback
To ensure quality and identify training needs, we use a public **Google Form** to capture coach feedback without requiring a RefTown login.

- **The Mechanism:** 
  1. Create a Google Form (e.g., "{{ league_name }} Umpire Feedback").
  2. Include fields for: Game Date, Field, Umpire Name, and a 0-3 Rating.
  3. **The Link:** Include the public link to this form in ALL manual BCC emails sent to coaches.
- **The UIC's Role:**
  - **Weekly Audit:** Review Form responses.
  - **Positive Reinforcement:** Forward "Excellent" ratings to the youth umpire (and their parents) to build morale.
  - **Constructive Intervention:** If a "Needs Improvement" rating comes in, cross-reference it with the game report. Reach out to the umpire to offer coaching or pair them with a veteran for their next assignment.
- **The Boundary:** Remind coaches (via BCC email text) that this form is for *developmental feedback* and rule clarification, not for protesting judgment calls.
[[ ENDIF ]]

[[ IF assignment_tool == 'ArbiterSports' ]]
## ArbiterSports: Professional Scheduling
ArbiterSports is used for high-reliability assigning with powerful automated conflict detection.

### Critical Workflows
1. **Auto-Assign Rules:** Configure your "Schedule Settings" in the Arbiter Dashboard to prioritize {{ league_name }} veterans for post-season and divisional games.
2. **Official Ratings:** Use the "Rating" tool weekly to group umpires by skill level (Pro, Intermediate, Junior). 
3. **Availability Blocks:** Train your umpires to use the Arbiter Mobile App to set their availability blocks before the 15th of each month.
4. **Self-Assign Option:** For junior leagues, you can enable "Self-Assign" to let youth umpires pick their own slots, drastically reducing your manual email load.
[[ ENDIF ]]

[[ IF assignment_tool == 'Assignr' ]]
## Assignr: Modern & Mobile
Assignr is optimized for youth leagues who prioritize mobile ease-of-use and integrated electronic payments.

### Critical Workflows
1. **In-App Payments:** Once a game is marked "Completed" in the app, the {{ rate_solo }} or standard pay is queued automatically. 
2. **Conflict Checking:** Assignr prevents double-booking across venues automatically, ensuring your officials aren't stretched too thin.
3. **Communication Centre:** Use the "Broadcast" feature to send mass text alerts for rainouts or last-minute field changes.
[[ ENDIF ]]

[[ IF assignment_tool == 'Horizon Web Ref' ]]
## Horizon Web Ref: Coordination & Training
Horizon is a robust platform that excels at document sharing and calendar synchronization.

### Critical Workflows
1. **Library Management:** Upload this Handbook PDF to the Horizon "Document Library" for easy umpire access.
2. **SMS Alerts:** Ensure the "SMS Notification" feature is enabled for 24-hour automatic reminder pings to officials.
3. **Evaluations:** Use the "Evaluation Form" creator to standardize feedback for junior umpires during the season.
[[ ENDIF ]]

[[ IF assignment_tool == 'Google Sheets' ]]
## Google Sheets: Manual Operations
For leagues using the "Lean" model, a collaborative Google Sheet is our central brain.

### Critical Workflows
1. **Master Schedule Structure:** Maintain one "Master" tab for games and a "Protected" tab for umpire contact info and historical pay rates.
2. **Data Validation:** Use dropdown lists for umpire names to prevent typos and ensure your `VLOOKUP` formulas for contact info don't break.
3. **Conflict Checking:** Use Conditional Formatting to highlight umpires scheduled for two games at the same time across different fields.
4. **Public View:** Use `IMPORTRANGE` to provide a "View-Only" version of the schedule to coaches.
[[ ENDIF ]]

[[ IF assignment_tool == 'Generic Association' ]]
## Local Association Portal (GTO, PBUA, NYBUA, etc.)
You are working with a regional umpire association that manages assignments via their own custom portal.

### Critical Workflows
1. **The Weekly Sync:** Contact the Association Assignor ({{ assoc_assignor_name }}) every Monday morning to confirm coverage for the upcoming week.
2. **Portal Access:** Log in to the association dashboard at [{{ assoc_portal_url }}]({{ assoc_portal_url }}) to verify official names and phone numbers.
3. **Vetting:** Regularly check the portal to ensure association veterans are assigned to sensitive inter-league or tournament matches.
4. **Conflict Resolution:** If a game is dropped by the association, immediately notify the Board and implement the "Coach Coverage" backup plan.
[[ ENDIF ]]

---

# 3. Data Integration: Schedule Imports
The success of a schedule import is 90% preparation. Since scheduling interfaces change frequently, always refer to the official guides for the most accurate step-by-step instructions.

### The "Universal Truths" of Importing
1. **Phase 1: Pre-Import Cleanup**
    - **Close the Season:** Use your platform's administrative tools to clear old slots before importing the new season.
    - **Create Teams & Coaches:** Ensure all teams and coaches exist in the database *before* you upload the CSV/Excel file. This links contact info to games instantly.
2. **Phase 2: The "Exact Match" Rule**
    - **Spelling is Absolute:** Platforms are unforgiving. "{{ local_park_example }}" in your sheet must match "{{ local_park_example }}" in the database exactly. One extra space will create "Ghost Fields."
    - **Synchronization:** If your platform supports ID-based imports (like RefTown or Arbiter), use the platform's provided template ONLY.

### Official Import Documentation
- [RefTown: Importing Games from Excel/CSV](https://reftown.com/kbp/index.php?category=9)
- [ArbiterSports: Official Game Import Guide](https://arbitersports.zendesk.com/hc/en-us/articles/209930747-Importing-Games-Overview)
- [Assignr: How to Import Games in Bulk](https://help.assignr.com/hc/en-us/articles/204212975-How-to-Import-Games)
- [Horizon Web Ref: Spreadsheet Import Guide](https://help.horizonwebref.com/articles/importing-games-via-spreadsheet)

---

# 4. Crisis Management: Rainouts & Cancellations

## The Field Status Rule
- **Monitoring:** Watch your local field status app or agency website like a hawk. 
- **The Link:** [{{ agency_name }} Field Status]({{ field_status_link }})
- **The Hotline:** If the digital status is down, call the {{ agency_name }} Field Condition Hotline at **{{ field_hotline }}**.
- **The Update:** Ensure you check for updates by the designated daily deadline (e.g., {{ status_deadline }}). 
- **Action:** If fields are closed, cancel games in your assignment platform immediately. Do not wait for coach consensus.

## Show-up Pay
- **The Rule:** If an umpire travels to the field because the cancellation wasn't communicated in a "fair" amount of time, the league MUST pay them. Proactive monitoring saves the budget.

---

# 5. Financials: Pay & Payroll

## Pay Rates
- **Plate Umpire:** {{ rate_plate }}
- **Base Umpire:** {{ rate_base }}
- **Solo Game:** If an umpire works a game solo, they work the plate and the rate is {{ rate_solo }}.

## Unassigned Games (The Backup Plan)
If the internal pool cannot produce an umpire for a game, the following protocol applies:
- **Coach/Assistant Officiating:** The head coach or an assistant coach from the participating teams must officiate the game.
- **The Philosophy:** Shift the focus from "winning" to the experience. It is about the kids having a game to play, not about a coach winning a divisional title. 
- **No External Outsource:** We do not use external contracting services (like GTO) unless explicitly authorized by the Board. The program relies on internal volunteers and the willingness of coaches to step in when needed.

## Payroll Cycle & Process
- **Cycle:** **Monthly**. While umpires often request bi-weekly pay, the current policy is monthly to manage the administrative workload for the UIC and the Treasurer.
- **Payment Method:** **Physical Checks**. Check the specific electronic payment options if using Assignr or Arbiter (ArbiterPay).
- **The "Ugh" Factor:** Physical checks are sent via USPS and typically take **10 days** to arrive after being cut. Successors should manage umpire expectations accordingly.
- **UIC Role:** At the end of each month, generate the payroll report in {{ assignment_tool }} and submit it to the Treasurer. Verify every game for solo-rate adjustments ({{ rate_solo }}) before submission.

---

# 6. Coach Relations & Boundaries

## The Transparency Loop (Targeted Needs)
- **Protocol:** Communicate with the pool only when specific game slots need to be filled. Avoid "blanket" emails that don't have actionable open games.
- **Respect the Inbox:** Umpires are volunteers; over-communicating can lead to them marking your emails as spam. Keep messages brief and focused on the "Open Games" list.

## Zero Tolerance & Privacy
- **The Boundary:** Coaches are strictly forbidden from texting umpires or parents directly to solicit coverage.
- **Privacy Protection:** The umpire pool's contact information is shared for the sole purpose of game management. Coaches must respect the privacy of officials.
- **Solicitation Policy:** Any coach found using platform data for unsolicited "side-deals" or pestering umpires will face immediate disciplinary action.
- **Privacy Protection:** You are the sole curator of the pool; you protect their information so they can focus on the game.

## The Philosophy
- **Coaches as Partners:** Coaches are co-educators. They call time to teach rules (Infield Fly, uncaught 3rd Strike) on the field, ensuring a fair and instructional environment.
- **Strike Zone First:** Get new recruits behind the plate early in lower-stakes games.

---

# 7. Field Logistics & Safety

## The "Plate Pack" (Equipment)
- **Umpire Gear:** Ensure the league has at least 3 sets of properly sized chest protectors, shin guards, and masks in the "Umpire Locker" at {{ local_park_example }}.
- **Sanitation:** Provide disinfectant wipes and hand sanitizer in the locker for gear turnover between games.

## Safety & The "Guardian Rule"
- **Supervision:** Every youth umpire without a parent on-site must have a designated "Board Member of the Day" (MOD) as their guardian.
- **Check-In:** The MOD must introduce themselves to the youth umpire before the game.
- **Night Games:** No youth umpire walks to their car alone.
- **Hydration:** During tournaments, ensure a cooler of water is available for umpires.
- **Injury Reporting:** Any on-field official injury must be reported to the UIC and Safety Officer within 2 hours.

---

# 8. Divisional Differences (Cheat Sheet)

| Division | Pitching Distance | Base Distance | Game Length |
| :--- | :--- | :--- | :--- |
| **Majors** | 46' | 60' | 6 Innings |
| **Minors** | 46' | 60' | 6 Innings |
| **Rookies** | 35' (Machine) | 60' | 5 Innings |

---

# 9. Master Rules & Limitations

### Pitching Limitations (Standard)
| Age Range | Max Pitches/Day |
| :--- | :--- |
| 13-16 | 95 |
| 11-12 | 85 |
| 9-10 | 75 |
| 7-8 | 50 |

### Rest Requirements (Days)
- **66+ Pitches:** 4 Days Rest.
- **51-65 Pitches:** 3 Days Rest.
- **36-50 Pitches:** 2 Days Rest.
- **21-35 Pitches:** 1 Day Rest.
- **1-20 Pitches:** 0 Days Rest.

### The International Mandate (Rule 0.07 / Regulation VI)
Be absolutely clear: Pitch count limits are **not local league suggestions**. They are **Little League International mandates**.
- **The "Safety First" Foundation:** These rules exist to prevent permanent orthopedic injuries (Little League Elbow). Ignoring them is negligence.
- **Consequences:** Violation results in immediate forfeit, manager suspension, and potential post-season disqualification.

---

# 10. GameChanger (GC) Integration
While your assignment platform manages umpires, **GameChanger** is for the league's families.

### Technical Workflows
- **League View:** Always perform game imports at the **Organization/League** level. Do **not** manage schedules on a per-team basis.
- **The SportsConnect Warning:** **Do not** import the master schedule into SportsConnect. This causes cascading errors/duplicates in GC.
- **Accuracy Audit:** Randomly check live games on the GC app to ensure pitch counts are being recorded. This is your primary defense against over-use violations.
- **Scorekeeper Training:** The UIC should host a "GC & Rules Clinic" for parents to ensure pitch counts are tracked accurately and consistently.
- **Defense Position Numbers:** **1:** P | **2:** C | **3:** 1B | **4:** 2B | **5:** 3B | **6:** SS | **7:** LF | **8:** CF | **9:** RF.

---

# 11. Appendix & Resources

## District Support
- **District:** Little League District {{ district_number }}
- **District UIC:** {{ district_uic_name }}
- **Contact:** [{{ district_uic_email }}](mailto:{{ district_uic_email }})

## Official Documentation
- **LL University:** [LL University - Umpire Portal](https://www.littleleague.org/university/umpires/)
- **Rulebook App:** Search for "Little League Rulebook" in the Apple App Store or Google Play Store.

### Platform Support Center Links
- [RefTown Support Center](https://reftown.com/kbp/index.php)
- [ArbiterSports Help](https://arbitersports.zendesk.com/)
- [Assignr Help Center](https://help.assignr.com/)
- [Horizon Web Ref Help](https://help.horizonwebref.com/)

---
*Template Version. Dedicated to Volunteer Excellence.*
