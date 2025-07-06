##### **Scenario:**

* You are an **IT specialist** working in a **medium-sized company**.
* Your **manager** wants a **daily report** to track machine usage.
* The report should show **which users are connected to which machines** at a given time.
* It’s **your job** to create this report.





##### **Existing System:**

* The company has a system that **collects events** from all networked machines.
* This system records:

&nbsp;	Each **user login**

&nbsp;	Each **user logout**

* The system provides this **event data** for reporting.





##### **Task Goal:**

**Write a script that:**

&nbsp;	Generates a report of **which users are logged into which machines** at that time.

&nbsp;	Outputs the report to the **screen**.

**Input Details:**

* The input is a **list of events**.
* Each event is an **instance of an Event class**.
* Each Event object contains:

&nbsp;	`date` – when the event happened

&nbsp;	`machine` – machine name where it happened

&nbsp;	`user` – user involved

&nbsp;	`type` – event type (`login` or `logout`)

* We care only about events with type `login` and `logout`.





##### **Output Details:**

* The report should:

&nbsp;	**List all machine names**.

&nbsp;	Under each machine, list the **users currently logged in**.

&nbsp;	**Format suggestion**: `machine\_name: user1, user2, user3`

&nbsp;	Keep the report format **simple first**, focus on correctness before appearance.





##### **Problem Summary:**

* **Process** a list of Event objects.
* **Use** the `date`, `machine`, `user`, and `type` attributes.
* **Generate** a report showing:

&nbsp;	Each machine

&nbsp;	All users currently logged into that machine





##### **Next Step:**

Research and plan how to **implement the solution** efficiently.

