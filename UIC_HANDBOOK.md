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

# 2. RefTown Mastery: Season Setup & Management

## Registration & Onboarding
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

## Handling Inquiries & Recruitment
You will receive automated emails from **RefTown Feedback** (Subject: "Umpiring little league"). These are high-value leads, often former players from your local high schools.

- **The "High-Value" Lead:** Former players are your best recruits. They know the fields, the culture, and the game.
- **Response Template:**
  > "Hello [Name], thanks for reaching out! It's great to hear you played at {{ league_abbreviation }}. We'd love to have you back in blue. To get started, please register here: {{ registration_link }}. Once you've signed up, I'll send you the info for the next training session and how to self-assign games. Welcome back!"
- **The Follow-up:** Don't just send the link. Mention the competitive pay rates—for a high schooler, this is the best hourly wage they can find.

## Schedule Import & Preparation
The success of a schedule import is 90% preparation. If the data doesn't match the RefTown database perfectly, the "Umpire Hawk" will spend hours manually fixing ghost entries.

- **Phase 1: Pre-Import Cleanup**
    - **Close the Season:** Use **Admin -> New Season Setup** to clear active slots.
    - **Create Teams:** Manually build or update the team list for the current season.
    - **Assign Coaches:** Include the coach's email and phone number. This is critical for RefTown's automated system, which sends coaches a summary email letting them know if an umpire has been assigned to their game or not.
- **Phase 2: The "Exact Match" Rule**
    - **Spelling is Absolute:** RefTown is unforgiving. "{{ local_park_example }} - [Field #]" is not the same as "{{ park_shortcut_example }}." "{{ division_example }} Red" is not the same as "Red Team."
    - **Synchronization:** The spelling in your import spreadsheet **must match** what you manually created in Phase 1. If it doesn't match, RefTown will either reject the row or create "Ghost Teams" that aren't linked to your coaches.
- **Phase 3: The Import Path**
    - Navigate to **Schedules -> Game Management -> Import New Games from Excel/CSV**.
    - **Template:** Use the official RefTown template ONLY.
    - **RefTown ID:** Leave **blank** for new games.
- **Official Reference:** Log in to RefTown, go to **Support**, and search the Knowledge Base for **"Importing Games"** to find the latest spreadsheet templates and field mappings.

## Assignment Lifecycle & Communication
Once the schedule is live, the "Second Season" begins: the hunt for coverage.

1. **The Request:** Umpires browse the schedule and "Request" games. They are not yet assigned; the game appears as "Requested" in the pool.
2. **The Assignment:** The UIC reviews requests and assigns the umpire. 
   - **UIC Tip:** Prioritize youth umpires for lower-division games to build their confidence.
3. **The Confirmation:** Once the UIC assigns the umpire, RefTown sends an automated notification to the **Coach**. This is the coach's signal that their game is covered.

## The "No Self-Unassign" Protocol
This is a critical policy for maintaining schedule integrity.
- **The Rule:** Once an umpire is assigned to a game, they **cannot** un-assign themselves in RefTown.
- **The Process:** The umpire must contact the UIC directly via email/text to request a drop.
- **The Rationale:** This prevents "Silent Gaps." When an umpire contacts you to drop, it triggers the UIC to immediately blast the pool for coverage. If they could drop silently, a game might go uncovered without the UIC ever knowing.

## Umpire Grading & Coach Feedback
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

---

# 3. Crisis Management: Rainouts & Cancellations

## The Field Status Rule
- **Monitoring:** Watch your local field status app or agency website like a hawk. 
- **The Link:** [{{ agency_name }} Field Status]({{ field_status_link }})
- **The Hotline:** If the digital status is down, call the {{ agency_name }} Field Condition Hotline at **{{ field_hotline }}**.
- **The Update:** Ensure you check for updates by the designated daily deadline (e.g., {{ status_deadline }}). 
- **Action:** If fields are closed, cancel in RefTown immediately. Do not wait for coach consensus.

## Show-up Pay
- **The Rule:** If an umpire travels to the field because the cancellation wasn't communicated in a "fair" amount of time, the league MUST pay them. Proactive monitoring saves the budget.

---

# 4. Financials: Pay & Payroll

## Pay Rates
- **Plate Umpire:** {{ rate_plate }}
- **Base Umpire:** {{ rate_base }}
- **Solo Game:** If an umpire works a game solo, they work the plate and the rate is {{ rate_solo }}.

## Unassigned Games (The Backup Plan)
If the internal pool cannot produce an umpire for a game, the following protocol applies:
- **Coach/Assistant Officiating:** The head coach or an assistant coach from the participating teams must officiate the game.
- **The Philosophy:** Shift the focus from "winning" to the experience. It is about the kids having a game to play, not about a coach winning a divisional title. 
- **No External Outsource:** We do not use external contracting services (like GTO). The program relies on internal volunteers and the willingness of coaches to step in when needed.

## Payroll Cycle & Process
- **Cycle:** **Monthly**. While umpires often request bi-weekly pay, the current policy is monthly to manage the administrative workload for the UIC (RefTown reports) and the Treasurer (check cutting).
- **Payment Method:** **Physical Checks**. We do not use direct deposit.
- **The "Ugh" Factor:** Checks are sent via USPS and typically take **10 days** to arrive after being cut. Successors should manage umpire expectations accordingly.
- **UIC Role:** At the end of each month, generate the payroll report in RefTown and submit it to the Treasurer. Verify every game for solo-rate adjustments ({{ rate_solo }}) before submission to avoid payment errors that take another month to fix.

---

# 5. Coach Relations & Boundaries

## The Transparency Loop (Targeted Needs)
- **Protocol:** Communicate with the pool only when specific game slots need to be filled. Avoid "blanket" emails that don't have actionable open games.
- **Respect the Inbox:** Umpires are volunteers; over-communicating can lead to them marking your emails as spam. Keep messages brief and focused on the "Open Games" list.
- **Manual BCC:** BCC the teams (coaches) on these manual pool requests when a game is in jeopardy of being uncovered. This gives coaches visibility into your efforts and prevents "Are we covered?" inquiries.
- **System Automation:** Note that RefTown automatically notifies assigned coaches and umpires. Your manual emails should only bridge the gap for unassigned games or last-minute drops.

## Zero Tolerance & Privacy
- **The Boundary:** Coaches are strictly forbidden from texting umpires or parents directly to solicit coverage.
- **Privacy Protection:** The umpire pool's contact information is shared in RefTown for the sole purpose of game management. Coaches must respect the privacy of officials.
- **Solitication Policy:** Any coach found using RefTown data for unsolicited "side-deals" or pestering umpires will face an immediate suspension of umpire assignments for their team. You are the sole curator of the pool; you protect their information so they can focus on the game.
- **The Penalty:** Formal report to the Board and removal of assigned umpires for the offending team's upcoming games.

---

# 6. Safety & The "Guardian Rule"

## Supervision
- **The Rule:** Every youth umpire without a parent on-site must have a designated "Board Member of the Day" (MOD) as their guardian.
- **Check-In:** The MOD must introduce themselves to the youth umpire before the game.
- **Night Games:** No youth umpire walks to their car alone.

---

## The Philosophy
- **Coaches as Partners:** Coaches are co-educators. They call time to teach rules (Infield Fly, uncaught 3rd Strike) on the field, ensuring a fair and instructional environment.
- **Strike Zone First:** Get new recruits behind the plate early in lower-stakes games.

## District 4 & Little League Resources
The following resources are provided by District 4 and Little League International for year-round development:
- **[Little League Umpire Registry](https://www.littleleagueumpire.org/):** Sign up for free access to videos, training aids, and announcements.
- **[Little League University - Umpire Portal](https://www.littleleague.org/university/umpires/):** The primary hub for all training. Search for **"Stance Basics"** or **"Three Steps"** to find the latest ball/strike positioning guides.
- **The Rulebook App:** Search for "Little League Rulebook" in the Apple App Store or Google Play Store to install the official rules and 2026 updates on your mobile device.
- **District Clinics:** Watch for emails from the District UIC regarding the annual Free Mechanics Clinic and regional training events.

---

# 8. Umpire Field Guide (Cheat Sheet)
This guide is your tactical manual on the field. Be BRIEF, be LOUD, and be ASSERTIVE.

## Plate Positioning & Mechanics
- **The "Slot":** Position yourself in the space between the catcher and the batter.
- **Locked Position:** Get set as the pitcher prepares. Hands behind the catcher to protect them.
- **Clearing the Catcher:** Once the ball is hit, "open the gate" by stepping back/out to let the catcher move. Follow the play toward 1st if needed.

## Base Positioning (60ft Diamond)
- **The Outside Theory:** In Little League (where no leading off is allowed), base umpires start **outside** the infield.
- **Position A:** Foul territory, 10-15 feet behind 1st base (No runners on).
- **Positions B & C:** On the **outfield grass** behind the infielders (Runners on).
  - **Position B:** Behind the second baseman, midway between 1st and 2nd.
  - **Position C:** Behind the shortstop, midway between 2nd and 3rd.
- **The "Library":** This is your working area *inside* the diamond. You only move into the library **after** the ball is put in play to gain the best angle for force plays or tags.

## Verbal & Physical Signals
| Situation | Verbal | Physical |
| :--- | :--- | :--- |
| **Strike** | "Strike!" | Right hand forward (pounding the wall). |
| **Ball** | "Ball!" | (No signal). Use LH fingers for count. |
| **Full Count** | "Full Count!" | 3 fingers LH / 2 fingers RH (Do NOT bump fists). |
| **Outs** | "Out!" | Fist pump or point. |
| **Safe** | "Safe!" | Arms spread wide. |
| **No Tag** | "No tag!" | Safe motion. |

## Complex Scenarios
- **1st to 3rd Coverage:** Plate umpire covers 3rd on a base hit with R1. Use hand signals to coordinate who has the bag.
- **Timing Plays:** Plate umpire initiates signal; Base umpire **must echo** it back.
- **Rundowns:** Stay out of the path. Split the field in half with your partner. Eye contact is essential. If you have the best angle, pat your chest and shout "Partner, I’ve got this—Out!"

## The Plate Meeting Checklist (The Game's Foundation)
The first 5 minutes sets the tone for the entire game. Be authoritative, brief, and clear.

- **Equipment Confirmation:** Confirm both managers have inspected their equipment. (Reminder: Non-LL/Illegal bats = Immediate discovery ejection).
- **Timing & The "Roll-back":**
    - **Identify the Official Clock:** The Plate Umpire’s watch is the only clock that matters. State the start time loudly for both scorekeepers.
    - **No New Inning:** Confirm the time limit (e.g., {{ time_limit }}). Remind teams that a new inning starts the *instant* the 3rd out of the previous inning is recorded.
    - **Hard Stop/Drop Dead:** If using a "Drop Dead" stop, confirm if the score **rolls back** to the last completed inning. Agreement here prevents post-game protests if a team is rallying when the clock expires.
- **Ground Rules (The "Dead Ball" Boundary):**
    - **Identify the Boundaries:** Walk the managers to the edge of the dugout. Identify where the permanent fence ends.
    - **The Imaginary Line:** If fields are unfenced, establish a clear dead-ball line (e.g., "From the end of the backstop to the dugout corner, then an imaginary straight line to the outfield light pole").
    - **Obstructions:** Note how to handle balls hitting trees, equipment buckets in the dugout path, or loose equipment on the field.
- **Final Command:** "I'm here for the kids. If you have a rule clarification, call time. If you have a judgment disagreement, let it go. Shake hands, and let's have a clean game."

---

# 9. GameChanger (GC) Integration
While RefTown is for umpires, **GameChanger** is for the league's families. As the "Tech UIC," you ensure these two worlds talk to each other.

## Organization-Level Management
- **The League View:** Always perform game imports at the **Organization/League** level. Do **not** manage schedules on a per-team basis.
- **The SportsConnect Warning:** **Do not** import the master schedule into SportsConnect. Because of the "one-way sync" nature of the platform, manual imports into SportsConnect can cause cascading errors or duplicates.
- **GC League Structure:** Import games only into the designated GameChanger leagues. There is a separate league for each division where we provide umpires (Uppers only: AAA, Minors, and Majors).
- **Schedule Parity:** Importing to the Org level in GC ensures that every team, coach, and parent sees the same "Source of Truth" that matches your RefTown master schedule.
- **Direct Alerts:** Use GC `Cancel & Message Team` (at the Org level) for rainouts to notify all stakeholders across the league simultaneously.
- **Scorekeeper Training:** Because GC is the official book, the UIC should host a "GC & Rules Clinic" for parents to ensure pitch counts are tracked accurately and consistently.

---

# 10. Pitch Count Enforcement & Auditing

Pitch counts are the most critical safety rule in Little League. As UIC, you aren't just managing umpires; you are the auditor-in-chief of arm safety.

## The UIC's Audit Role
While managers are responsible for their pitchers, the UIC must verify compliance to prevent protests and season-ending injuries.
- **Weekly GC Audit:** Use the **"League Pitch Count Report"** in GameChanger (Organization Admin view). 
- **What to look for:**
  - **Rest Threshold Violations:** Did a pitcher throw 66+ pitches and return before 4 days of rest?
  - **Catcher/Pitcher Conflicts:** A player who catches 4+ innings cannot pitch that day. A pitcher who throws 41+ pitches cannot catch.
- **The "Safety First" Correction:** If an audit reveals a violation, notify the Board President and the affected managers immediately. Safety overrides any game result.

## Training Parent Scorekeepers
Scorekeepers are often hard to find and nervous about the rules. The UIC should simplify their job:
- **The "Official" Source:** Remind parents that the **Home Team's GameChanger** is the official record.
- **Umpire Support:** Train your umpires to ask the scorekeeper for the count between every half-inning. This "Public Verification" prevents discrepancies from exploding in the 6th inning.
- **Cheat Sheets:** Provide a physical "Rest Requirements" card (laminated) to every scorekeeper booth.

## The International Mandate (Rule 0.07 / Regulation VI)
Be absolutely clear: Pitch count limits are **not local league suggestions**. They are **Little League International mandates**.
- **The "Safety First" Foundation:** These rules exist to prevent permanent orthopedic injuries (Little League Elbow). Ignoring them is not "competitiveness"—it is negligence.
- **Liability:** Failure to enforce these rules can expose the League Board to significant liability and potential loss of insurance coverage if a player is injured while pitching in violation of rest requirements.

## Consequences of Non-Compliance
Violation of pitching regulations is a non-negotiable infraction that results in the following:
1. **Immediate Forfeit:** If a protest is upheld by the Protest Committee, the game is declared a **forfeit** in favor of the opposing team, regardless of the score.
2. **Manager Suspension:** The manager of the offending team faces a **mandatory suspension** (minimum one game).
3. **Double Ineligibility:** The pitcher whose violation triggered the event is ineligible to pitch in the game for which the manager is suspended.
4. **Post-Season Impact:** Documented failures to manage pitch counts can disqualify an entire team or manager from post-season (All-Stars) selection.

## Pitching Limitations & Rest Reference
Scorekeepers must track pitches and alert the head coach when a pitcher is within 15 pitches of their limit. **Accuracy is critical: exact pitch counts dictate required rest days and protect player arms.**

### Daily Pitch Limits
| Age Group | Daily Pitch Limit |
| :--- | :--- |
| **7-8 Years** | 50 pitches per day |
| **9-10 Years** | 75 pitches per day |
| **11-12 Years** | 85 pitches per day |

### Required Rest Days
| Pitches Thrown | Required Rest Days |
| :--- | :--- |
| **1 - 20** | 0 Calendar Days |
| **21 - 35** | 1 Calendar Day |
| **36 - 50** | 2 Calendar Days |
| **51 - 65** | 3 Calendar Days |
| **66+** | 4 Calendar Days |

*Note: A pitcher may finish the current batter if the limit is reached during an at-bat.*

### Defense Position Numbers (GameChanger)
**1:** Pitcher | **2:** Catcher | **3:** 1st Base | **4:** 2nd Base | **5:** 3rd Base | **6:** Shortstop | **7:** Left Field | **8:** Center Field | **9:** Right Field

---


# 11. Resources & Regional Support

The UIC role is demanding, but you are part of a larger network. Use these resources when you need a "Second Opinion" on a rule or board policy.

## District Support
- **District:** Little League District {{ district_number }}
- **District UIC:** {{ district_uic_name }}
- **Contact:** [{{ district_uic_email }}](mailto:{{ district_uic_email }})

## Official Documentation
- **LL University:** The gold standard for rules education. [LL University Portals](https://www.littleleague.org/university/)
- **RefTown Support:** For technical issues with the assignment platform. [RefTown Support Center](https://reftown.com/kbp/index.php)

---
*Template Version. Dedicated to Volunteer Excellence.*
