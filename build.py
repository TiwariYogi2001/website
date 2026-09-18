"""
Site generator for Yogesh Tiwari's portfolio.

Edit the content in this file, then run:

    python build.py

It rewrites every .html page (plus sitemap.xml and robots.txt) so the header,
footer and SEO tags stay identical everywhere. CSS lives in assets/css/style.css
and behaviour in assets/js/main.js.
"""

from pathlib import Path
from html import escape
import hashlib

ROOT = Path(__file__).parent
SITE = "https://tiwariyogi2001.github.io/website/"
NAME = "Yogesh Tiwari"
EMAIL = "yogeshtiwari8974@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/yogesh-tiwari2000"
GITHUB = "https://github.com/TiwariYogi2001"
WHATSAPP = "https://wa.me/qr/6AC4PS544CA7A1"
RESUME = "assets/Yogesh_Tiwari_Resume.pdf"
GH = "https://github.com/TiwariYogi2001/"

NAV = [
    ("index", "index.html", "Home"),
    ("about", "about.html", "About"),
    ("experience", "experience.html", "Experience"),
    ("work", "work.html", "Work"),
    ("skills", "skills.html", "Skills"),
]


# =====================================================================
#  PROJECTS — each one becomes work/<slug>.html
# =====================================================================

CATS = {
    "market": "Market intelligence",
    "dashboard": "Dashboards",
    "sql": "SQL analysis",
    "build": "Games & XR",
}

PROJECTS = [
    {
        "slug": "steam-market-intelligence",
        "cat": "market",
        "title": "Steam market intelligence for studio outreach",
        "short": "Steam market intelligence",
        "card": "A 1,310-line Python scraper, 500+ Steam titles, and a scored lead pipeline behind a 30%+ reply rate.",
        "role": "BD &amp; Outreach Specialist, Brothers Interactive",
        "when": "Oct 2025 – present",
        "tools": ["Python", "Web scraping", "Pandas", "Excel", "Lead scoring"],
        "thumb": {"type": "funnel"},
        "figures": [("30%+", "reply rate (industry 5–10%)"), ("500+", "Steam titles analysed"),
                    ("100+", "studios &amp; publishers contacted"), ("1", "signed partnership")],
        "question": "Brothers Interactive sells outsourced art and development to game studios. Cold outreach in this "
                    "industry usually gets a 5–10% reply rate, because most messages are generic and land with studios "
                    "that have no current need. The question: <strong>which studios should we talk to, and what should we say "
                    "so they actually reply?</strong>",
        "data": "Public Steam store data for 500+ titles — genre and tags, pricing, release timing, review counts and how "
                "they trend, publisher and developer activity, and each studio's social presence. Collected with a "
                "custom Python script (1,310 lines) and joined into a single research dataset.",
        "approach": [
            ("Scrape", "Built a Python scraper to pull store-page and review data for 500+ titles, handling pagination, "
                       "missing fields and rate limits."),
            ("Enrich", "Cleaned and structured the data in Pandas: genre trends, price bands, review trajectories, "
                       "publisher activity and social links per studio."),
            ("Score", "Classified studios into tiers and scored leads in Excel, so outreach went to studios whose "
                      "pipeline and art style matched what we offer."),
            ("Reach out", "Wrote research-first messages across email, LinkedIn, Discord and gaming communities — each "
                          "one referencing the studio's own games and market position."),
            ("Track", "Maintained outreach dashboards for pipeline health, reply rates and tier conversion, and documented "
                      "the workflow as a repeatable playbook."),
        ],
        "findings": [
            "Research-first outreach earned a <strong>30%+ reply rate — 3–5× the 5–10% industry average</strong>.",
            "100+ indie studios, publishers and gaming companies contacted through a structured, qualified pipeline.",
            "One studio partnership taken from market identification all the way to a <strong>signed collaboration agreement</strong>.",
            "Playbooks, templates and research workflows documented so the process scales beyond one person.",
        ],
        "note": "Company data and partner names stay confidential; the figures above are the ones I share on my résumé.",
        "links": [],
    },
    {
        "slug": "visa-transaction-analysis",
        "cat": "dashboard",
        "title": "Visa — customer spending, fraud &amp; lifetime value",
        "short": "Visa transaction analysis",
        "card": "1.3M transactions: EDA, ten hypothesis tests, fraud patterns, RFM segments and a Tableau dashboard.",
        "role": "NextLeap fellowship graduation project",
        "when": "2025",
        "tools": ["Python", "Pandas", "Seaborn", "SciPy", "Tableau"],
        "thumb": {"type": "img", "src": "assets/img/projects/visa.webp", "w": 1599, "h": 899},
        "figures": [("$91.22M", "total spend analysed"), ("1.30M", "transactions"), ("1.00%", "fraud rate"),
                    ("$92.8K", "average CLV")],
        "question": "Growing the value of existing cardholders is cheaper than acquiring new ones. <strong>Which customers "
                    "drive transaction value, what makes them spend more, and where does fraud concentrate?</strong>",
        "data": "Card transactions from January 2019 to July 2020: customer demographics, merchant and category, amount, "
                "timestamp, cardholder and merchant location, and a fraud flag.",
        "approach": [
            ("Clean", "Dropped index artefacts, parsed dates, derived customer age, filled missing job and ZIP fields, "
                      "and documented every column."),
            ("Engineer", "Added hour, weekday and month features, plus the distance between cardholder and merchant — "
                         "a classic fraud signal."),
            ("Explore", "EDA on spend by category, weekday, hour, gender and month, with a correlation heatmap."),
            ("Test", "Ran ten hypothesis tests — e.g. do frequent users spend more, do weekend shoppers have higher CLV, "
                     "is fraud more likely between midnight and 6 AM, does merchant diversity raise CLV."),
            ("Segment", "Built RFM (recency, frequency, monetary) segments to separate Champions from at-risk and "
                        "dormant customers, then visualised it all in Tableau."),
        ],
        "findings": [
            "Most transactions happen <strong>between 12 PM and 3 PM</strong>; Sunday and Monday are the busiest days.",
            "By frequency, gas/transport, grocery and in-store shopping lead; by spend, grocery, online shopping and "
            "entertainment lead.",
            "Fraud clusters in the <strong>odd hours (12 AM – 6 AM)</strong> and in online shopping and grocery — and it "
            "spans low and high amounts, not just big tickets.",
            "RFM segments give marketing a ready target list: reward Champions, re-engage dormant high-value customers.",
        ],
        "recommend": [
            "Add time-of-day rules to fraud monitoring for the midnight–6 AM window.",
            "Apply category-level checks to online shopping and grocery transactions.",
            "Run weekend and multi-category campaigns aimed at the highest-CLV segments.",
        ],
        "links": [("Notebook &amp; PDF report", GH + "Visa-Transactioon-Analysis")],
    },
    {
        "slug": "flipkart-customer-service",
        "cat": "dashboard",
        "title": "Flipkart — what really drives customer satisfaction",
        "short": "Flipkart customer service",
        "card": "~30,000 support interactions: how sentiment, SLA, channel and call length move CSAT.",
        "role": "Case study",
        "when": "2025",
        "tools": ["Excel", "Power Query", "Pivot tables", "EDA", "Metric trees"],
        "thumb": {"type": "img", "src": "assets/img/projects/flipkart.webp", "w": 1280, "h": 537},
        "figures": [("29,997", "customers analysed"), ("4", "support channels"), ("3", "SLA bands")],
        "question": "Flipkart wants to keep customers after they contact support. <strong>Which parts of the support "
                    "experience actually move satisfaction and retention?</strong>",
        "data": "Customer-service interactions with sentiment, CSAT score, call duration, response time against SLA, "
                "channel (chatbot, email, call centre, web), issue type, and customer and call-centre location.",
        "approach": [
            ("Metric tree", "Broke satisfaction into four branches — customer satisfaction, service experience, issue "
                            "type, and geography — before touching the data."),
            ("Clean", "Standardised categories and bucketed calls into short, medium and long."),
            ("Analyse", "Compared CSAT and sentiment across SLA bands, channels, call lengths, issue types and states."),
            ("Dashboard", "Built an interactive Excel dashboard with slicers for sentiment, call centre, channel, reason "
                          "and response time, plus a CSAT map of India."),
        ],
        "findings": [
            "Sentiment is the strongest predictor of satisfaction — negative sentiment lines up with low CSAT and churn risk.",
            "Responses <strong>within SLA</strong> correlate with better CSAT; above-SLA cases drive negative feedback.",
            "The <strong>call centre outperforms chatbots</strong> on both CSAT and sentiment.",
            "<strong>Medium-length calls</strong> score best: short calls look rushed, long calls signal complexity.",
            "Billing and outage issues dominate volume, and CSAT varies noticeably by region.",
        ],
        "recommend": [
            "Prioritise SLA compliance on billing and outage tickets.",
            "Route complex issues from chatbot to call centre earlier.",
            "Investigate the weakest regions with localised support improvements.",
        ],
        "links": [("Excel workbook", GH + "Data-analysis-dashboard")],
    },
    {
        "slug": "madhav-ecommerce-dashboard",
        "cat": "dashboard",
        "title": "Madhav E-Commerce — sales &amp; profit dashboard",
        "short": "Madhav e-commerce",
        "card": "Revenue, profit and payment mix by state, category and customer — and the loss-making months.",
        "role": "Dashboard project",
        "when": "2025",
        "tools": ["Power BI", "Excel", "Data modelling", "Slicers"],
        "thumb": {"type": "img", "src": "assets/img/projects/madhav.webp", "w": 1280, "h": 722},
        "figures": [("₹438K", "sales"), ("₹37K", "profit"), ("5,615", "units sold"), ("43.7%", "orders paid by COD")],
        "question": "An online retailer has healthy revenue but thin profit. <strong>Where is the money made, where is "
                    "it lost, and who are the best customers?</strong>",
        "data": "Order and order-detail tables for a fictional e-commerce store: amount, profit, quantity, category, "
                "sub-category, customer, state, payment mode and date.",
        "approach": [
            ("Model", "Related the order and detail tables and built calculated measures for profit and average order value."),
            ("Visualise", "Bar, donut, clustered bar, line and area charts, with slicers to drill into any state or category."),
            ("Read", "Compared monthly profit, category mix, payment preferences and top customers."),
        ],
        "findings": [
            "<strong>Maharashtra</strong> leads sales at ₹100K+, followed by Madhya Pradesh and Uttar Pradesh.",
            "Clothing is 62.6% of units, electronics 20.6%, furniture 16.8%.",
            "Cash on delivery still leads payments at 43.7%, ahead of UPI at 20.6%.",
            "December is the best month, but <strong>May, June, July and October run at a loss</strong>.",
            "Printers (₹8.6K), bookcases (₹6.5K) and sarees (₹4.1K) are the most profitable sub-categories.",
        ],
        "recommend": [
            "Review pricing and discounting in the four loss-making months.",
            "Nudge COD buyers toward UPI to cut return and collection costs.",
            "Push high-margin sub-categories alongside high-volume clothing.",
        ],
        "links": [(".pbix file", GH + "Madhav-E-Commerce-Sales-Dashboard")],
    },
    {
        "slug": "personal-expense-dashboard",
        "cat": "dashboard",
        "title": "Personal finance — income, spending &amp; savings",
        "short": "Personal expense dashboard",
        "card": "A year of money in and out across 19 sub-categories, with monthly net saving.",
        "role": "Dashboard project",
        "when": "2025",
        "tools": ["Power BI", "DAX", "Power Query"],
        "thumb": {"type": "img", "src": "assets/img/projects/expense.webp", "w": 1280, "h": 714},
        "figures": [("₹1.57M", "income"), ("₹0.72M", "spending"), ("₹0.85M", "net saving"), ("19", "sub-categories")],
        "question": "<strong>Where does the money go each month, and when does spending overtake income?</strong> "
                    "A personal budget is a small dataset with the same questions a CFO asks.",
        "data": "A year of debit and credit transactions, categorised into 8 main categories and 19 sub-categories.",
        "approach": [
            ("Categorise", "Mapped every transaction into a two-level category tree."),
            ("Measure", "DAX measures for debit, credit and net saving by month."),
            ("Filter", "Slicers for category, sub-category and quarter so any slice can be isolated, e.g. "
                       "&ldquo;Q2 discretionary only&rdquo;."),
        ],
        "findings": [
            "Spending is <strong>less than half of income</strong>, leaving ₹0.85M net saving.",
            "Living expenses (₹393.6K) and discretionary spend (₹168.7K) are the biggest categories; rent, groceries "
            "and clothes top the sub-categories.",
            "April has the highest spending (₹83K); January the highest income (₹336K).",
            "<strong>November goes negative</strong> — expenses exceed income by ₹17.3K.",
        ],
        "links": [(".pbix file", GH + "Personal_expense_dashboard")],
    },
    {
        "slug": "pizza-sales-sql",
        "cat": "sql",
        "title": "Pizza sales — 13 business questions in SQL",
        "short": "Pizza sales SQL",
        "card": "From total revenue to window-function rankings across a four-table order dataset.",
        "role": "SQL case study",
        "when": "2025",
        "tools": ["MySQL", "JOINs", "Subqueries", "Window functions"],
        "thumb": {"type": "code", "lines": ["SELECT name, revenue", "FROM ( SELECT category, name,", "  RANK() OVER (PARTITION BY", "    category ORDER BY revenue"]},
        "figures": [("$817.9K", "revenue in 2015"), ("21,350", "orders"), ("49,574", "pizzas sold"), ("12–1 PM", "busiest hour")],
        "question": "A pizza shop wants to know <strong>what sells, when, and what earns the most</strong> — so it can "
                    "plan its menu, staffing and inventory.",
        "data": "Four related CSVs: orders (timestamps), order details (pizza and quantity), pizzas (size and price) and "
                "pizza types (name, category, ingredients).",
        "approach": [
            ("Basic", "Total orders and revenue, highest-priced pizza, most common size, top 5 pizzas by quantity."),
            ("Intermediate", "Quantity by category, orders by hour, daily average pizzas, top 3 by revenue."),
            ("Advanced", "Revenue share by category, cumulative revenue over time, and the top 3 pizzas per category "
                         "with <code>RANK() OVER (PARTITION BY …)</code>."),
        ],
        "findings": [
            "A full year (2015) of trading: <strong>21,350 orders, 49,574 pizzas and $817.9K revenue</strong> — about 138 pizzas a day.",
            "Orders peak at <strong>lunch, 12–1 PM</strong>, with a second rush from 5–7 PM — the two staffing windows that matter.",
            "Large is the most-ordered size; XL and XXL together are only about 1% of order lines.",
            "The Classic Deluxe sells the most units (2,453), but the <strong>Thai Chicken earns the most revenue</strong> ($43.4K) — volume and value aren't the same list.",
            "Revenue is spread evenly: Classic leads at 26.9%, and the other three categories sit between 23.7% and 25.5%.",
            "The Brie Carre is the weakest earner at $11.6K — a candidate for a menu review.",
        ],
        "recommend": [
            "Staff and prep for the lunch peak first, then the early-evening rush.",
            "Promote high-value chicken pizzas alongside the best-selling Classic Deluxe.",
            "Review or reposition the lowest-revenue pizzas, and consider dropping XXL.",
        ],
        "code": """-- Top 3 pizzas by revenue in each category
SELECT name, revenue
FROM (
  SELECT category, name, revenue,
         RANK() OVER (PARTITION BY category
                      ORDER BY revenue DESC) AS rn
  FROM (
    SELECT pt.category, pt.name,
           SUM(od.quantity * p.price) AS revenue
    FROM pizza_types pt
    JOIN pizzas p ON pt.pizza_type_id = p.pizza_type_id
    JOIN order_details od ON od.pizza_id = p.pizza_id
    GROUP BY pt.category, pt.name
  ) AS by_pizza
) AS ranked
WHERE rn <= 3;""",
        "links": [("Queries &amp; data", GH + "Pizza_sales_analysis")],
    },
    {
        "slug": "airbnb-sql-analysis",
        "cat": "sql",
        "title": "Airbnb — hosts, guests, bookings &amp; pricing",
        "short": "Airbnb SQL",
        "card": "Six analysis areas across listings, calendar and reviews, each ending in a recommendation.",
        "role": "SQL case study",
        "when": "2025",
        "tools": ["PostgreSQL", "CTEs", "Aggregations", "Excel"],
        "thumb": {"type": "code", "lines": ["SELECT host_name,", "  COUNT(*) AS listings,", "  AVG(review_scores_rating)", "HAVING COUNT(*) >= 2"]},
        "figures": [("419", "listings"), ("190", "hosts"), ("21", "property types"), ("29", "hosts with 4+ listings")],
        "question": "<strong>What separates high-performing Airbnb listings and hosts from the rest</strong> — and what "
                    "should the platform do about the gap?",
        "data": "Listings (host, property type, price, ratings), calendar (date-level availability and price) and reviews "
                "(reviewer and comments).",
        "approach": [
            ("Property diversity", "Listing counts and the top 5 property types."),
            ("Guest ratings", "Average scores, top 10 listings, and how many fall below 4.0."),
            ("Host engagement", "Multi-listing hosts, average score per host, and struggling hosts with 2+ listings."),
            ("Booking trends", "Occupancy rate per listing for January 2024, top performers and zero-booking listings."),
            ("Pricing", "Average nightly price by property type and budget-friendly categories under $150."),
            ("Reviews", "Most active reviewers, reviews per listing, and properties with no 2023 reviews."),
        ],
        "findings": [
            "The market (centred on Albany, NY) is dominated by <strong>entire rental units — 203 of 419 listings</strong>; "
            "together with entire homes, whole-place stays are 73% of supply.",
            "<strong>29 hosts run more than three listings</strong>, and the largest single host has 27 — their ratings "
            "move the whole market.",
            "Quality is high: only 10 of 359 rated listings score below 4.0, and 55% of listings belong to Superhosts.",
            "Zero-booking listings are identifiable from the calendar and are candidates for pricing and content fixes.",
        ],
        "recommend": [
            "Reward top hosts with badges and extra visibility; offer training to hosts below 4.0.",
            "Feature high-rated listings in discovery and marketing emails.",
            "Prompt post-stay reviews to lift listings with no recent feedback.",
        ],
        "code": """-- Hosts with 2+ listings but a rating below 4.0
SELECT host_name,
       COUNT(*)                  AS total_listings,
       AVG(review_scores_rating) AS avg_rating
FROM listings
WHERE review_scores_rating IS NOT NULL
GROUP BY host_name
HAVING COUNT(*) >= 2
   AND AVG(review_scores_rating) < 4.0
ORDER BY avg_rating;""",
        "links": [("Queries &amp; README", GH + "Airbnb_SQL_Analysis")],
    },
    {
        "slug": "ipl-performance-analysis",
        "cat": "sql",
        "title": "IPL — team performance across seasons",
        "short": "IPL performance",
        "card": "Win counts, run rates and bowling strength by team, straight from match data.",
        "role": "SQL case study",
        "when": "2025",
        "tools": ["PostgreSQL", "Python", "Tableau"],
        "thumb": {"type": "code", "lines": ["SELECT team,", "  ROUND(SUM(runs_scored)", "    / SUM(overs_faced), 2)", "  AS run_rate FROM ipl"]},
        "figures": [("950", "team innings"), ("15", "seasons, 2008–2022"), ("131", "Mumbai Indians wins"), ("653", "RCB wickets taken")],
        "question": "<strong>Which IPL teams are most efficient with the bat and the ball</strong>, and how do scoring "
                    "patterns relate to results?",
        "data": "Team-level match records: team and opponent, date, venue, season, runs scored and conceded, wickets "
                "lost and taken, overs faced, result and player of the match.",
        "approach": [
            ("Model", "Designed the table schema with a match-level primary key in PostgreSQL."),
            ("Results", "Win and loss counts, and average runs in winning versus losing matches."),
            ("Efficiency", "Run rate by team, low-wicket innings, and teams with 200+ wickets taken."),
            ("Visualise", "Explored consistency and season trends further in Python and Tableau."),
        ],
        "findings": [
            "<strong>Mumbai Indians win the most matches (131)</strong>, ahead of Chennai Super Kings (121) and Kolkata "
            "Knight Riders (114).",
            "Royal Challengers Bangalore take the most wickets (653) — yet sit fourth on wins, so bowling volume alone "
            "doesn't win titles.",
            "Winners average only about 4 more runs than losers (143.5 vs 139.7) — the total on its own rarely decides a match.",
            "Lucknow Super Giants top the run-rate table, but on just 97 overs; among long-running franchises, Rajasthan "
            "Royals lead. <strong>Sample size matters</strong> before ranking anyone.",
        ],
        "code": """-- Run rate by team
SELECT team,
       SUM(runs_scored)  AS runs,
       SUM(overs_faced)  AS overs,
       ROUND(SUM(runs_scored)::numeric
             / SUM(overs_faced), 2) AS run_rate
FROM ipl
GROUP BY team
ORDER BY run_rate DESC;""",
        "links": [("Queries &amp; data", GH + "Ipl_performance_analysis")],
    },
    {
        "slug": "music-store-sql",
        "cat": "sql",
        "title": "Music store — best customers, cities &amp; genres",
        "short": "Music store SQL",
        "card": "An 11-table store database: who spends most, where, and on what genres.",
        "role": "SQL case study",
        "when": "2025",
        "tools": ["PostgreSQL", "JOINs", "CTEs"],
        "thumb": {"type": "code", "lines": ["SELECT billing_city,", "  SUM(total) AS invoice_total", "FROM invoice", "ORDER BY invoice_total DESC"]},
        "figures": [("$4,709", "revenue analysed"), ("614", "invoices"), ("59", "customers"), ("24", "countries")],
        "question": "A digital music store wants to <strong>reward its best customers and plan a promotional music "
                    "festival</strong> in the right city.",
        "data": "Employees, customers, invoices and invoice lines, tracks, albums, artists, genres, media types and playlists.",
        "approach": [
            ("Basics", "Senior-most employee, invoices by country, top invoice totals."),
            ("Customers", "The best city by invoice total, and the single highest-spending customer."),
            ("Genres", "Rock listeners, top artists by track count, and the most popular genre in each country."),
        ],
        "findings": [
            "<strong>Prague is the festival city</strong>: $273 in invoices, well ahead of Mountain View ($169) and London ($166).",
            "The USA has the most invoices (131), followed by Canada (76) and Brazil (61).",
            "The single best customer spent $144.54 — the top three together account for 8% of all revenue.",
            "<strong>Rock dominates</strong> with 2,635 tracks sold, more than four times Metal in second place.",
        ],
        "code": """-- Where should we hold a promotional festival?
-- The city whose customers spend the most.
SELECT billing_city,
       SUM(total) AS invoice_total
FROM invoice
GROUP BY billing_city
ORDER BY invoice_total DESC
LIMIT 1;""",
        "links": [("Queries &amp; data", GH + "Music_Store_Analysis")],
    },
    {
        "slug": "schoolvr",
        "cat": "build",
        "title": "SchoolVR — immersive VR classrooms",
        "short": "SchoolVR",
        "card": "Subject-wise VR modules with engagement analytics for teachers.",
        "role": "AR/VR Executive, AICMUJ Innovation Foundation",
        "when": "2023 – 2025",
        "tools": ["Unity", "C#", "VR", "Analytics"],
        "thumb": {"type": "glyph", "label": "VR"},
        "figures": [("5+", "startup partners supported"), ("3+", "developers mentored")],
        "question": "Students remember what they experience. <strong>Could VR make science, history and geography "
                    "lessons stick — and could teachers see whether it works?</strong>",
        "data": "Built at the Atal Incubation Centre, Manipal University Jaipur, alongside startup partners and schools.",
        "approach": [
            ("Modules", "Subject-wise VR scenes that place learners inside the concept being taught."),
            ("Guidance", "Guided learning paths and simple controls so students of any age can use it."),
            ("Analytics", "Engagement and topic-mastery tracking so teachers can follow each student's progress."),
        ],
        "findings": [
            "Adding analytics turned a demo into a tool schools could evaluate — the moment I started caring about data.",
            "Coordinating design, development and client feedback taught me to translate between business and technical teams.",
        ],
        "links": [],
    },
    {
        "slug": "callbreak-multiplayer",
        "cat": "build",
        "title": "Callbreak — real-time multiplayer card game",
        "short": "Callbreak multiplayer",
        "card": "Bidding, scoring, bots and online matchmaking in Unity and Socket.io.",
        "role": "Unity Developer, Mobzway Technologies",
        "when": "2022 – 2023",
        "tools": ["Unity3D", "C#", "Socket.io", "QA"],
        "thumb": {"type": "glyph", "label": "♠"},
        "figures": [("4", "players per table"), ("Real-time", "networking")],
        "question": "Callbreak is a trick-taking card game popular in South Asia. <strong>Make it play smoothly online, "
                    "in real time, on mobile.</strong>",
        "data": "Part of Mobzway's 2D casino game portfolio.",
        "approach": [
            ("Rules", "Turn management, bidding logic, scoring rules and fair card distribution."),
            ("Multiplayer", "Online matchmaking and real-time communication between players over Socket.io."),
            ("Bots", "Bot players so tables fill and games continue when someone drops."),
            ("Polish", "Clean UI, animations, and performance tuning of game loops for mobile."),
        ],
        "findings": [
            "Debugging and QA across many builds — tracked in structured Excel logs — was my first real data habit.",
            "Building games first-hand is why I understand what studios need when I talk to them today.",
        ],
        "links": [("Mobzway", "https://www.mobzway.com/")],
    },
]

EXPERIENCE = [
    {
        "role": "BD &amp; Outreach Specialist",
        "org": "Brothers Interactive",
        "place": "Jaipur · on-site",
        "when": "Oct 2025 — present",
        "summary": "Business development, market research and analysis for a game art and development studio — finding "
                   "the studios we should work with, and turning research into conversations that land.",
        "stats": [("30%+", "reply rate"), ("100+", "studios contacted"), ("500+", "Steam titles analysed"), ("1", "partnership signed")],
        "bullets": [
            "Achieving a <strong>30%+ outreach reply rate — 3–5× the 5–10% industry average</strong> — with research-first "
            "messages across email, LinkedIn, Discord and gaming communities.",
            "Contacted <strong>100+ indie studios, publishers and gaming companies</strong>, running a structured pipeline "
            "from market research through qualification to partnership discussion.",
            "Scraped and analysed <strong>500+ Steam titles with a custom 1,310-line Python script</strong> — genre trends, "
            "pricing, review trajectories, publisher activity and social presence — to target BD.",
            "Closed <strong>one confirmed studio partnership</strong>, owning the full cycle from market identification to "
            "signed collaboration agreement.",
            "Gather requirements from B2B clients and internal teams, and map how the studio engages partners with workflow "
            "diagrams, process documentation and use cases.",
            "Act as the bridge between business teams (sales, marketing, operations) and technical teams (developers, product).",
            "Maintain outreach dashboards, lead-scoring datasets and KPI reports in Excel and Power BI for pipeline health, "
            "reply rates and studio tiers.",
            "Documented research workflows, outreach playbooks and templates so the BD process is repeatable.",
        ],
        "tags": ["Python", "SQL", "Excel", "Power BI", "Lead generation", "Market research"],
        "case": "steam-market-intelligence",
    },
    {
        "role": "Data Analyst Fellow",
        "org": "NextLeap",
        "place": "Remote",
        "when": "Apr — Aug 2025",
        "summary": "An intensive, project-based analytics fellowship on real business datasets. Graduated as a Top Fellow.",
        "stats": [("Top", "Fellow")],
        "bullets": [
            "Built interactive dashboards in Tableau and Power BI to analyse KPIs, trends and performance.",
            "Practised advanced SQL — JOINs, GROUP BY, CTEs and window functions — on real-world business data.",
            "Ran exploratory data analysis in Python, Pandas and Matplotlib and turned it into visual reporting.",
            "Delivered projects on customer segmentation, revenue forecasting and structured reporting workflows.",
            "Improved data cleaning and transformation steps to produce dashboard-ready datasets.",
        ],
        "tags": ["SQL", "Python", "Tableau", "Power BI", "EDA"],
        "case": "visa-transaction-analysis",
    },
    {
        "role": "AR/VR Executive",
        "org": "AICMUJ Innovation Foundation",
        "orgfull": "Atal Incubation Centre, Manipal University Jaipur",
        "place": "Jaipur · on-site",
        "when": "Mar 2023 — Apr 2025",
        "summary": "Led immersive AR/VR projects for startups incubated at Manipal University Jaipur — from founder "
                   "workshop to working prototype.",
        "stats": [("5+", "startup partners"), ("10+", "strategy workshops"), ("3+", "developers mentored")],
        "bullets": [
            "Led development of immersive AR/VR solutions for <strong>5+ startup partners</strong>, coordinating delivery "
            "and cross-team alignment across the development cycle.",
            "Ran <strong>10+ business strategy workshops</strong> with founders on how emerging tech could solve "
            "industry-specific problems.",
            "Tracked project KPIs and operational metrics in Excel dashboards, and integrated Python, Power BI and "
            "Tableau analytics into XR projects to support product decisions.",
            "Mentored <strong>3+ junior developers</strong> on Unity and XR integration, speeding up team delivery.",
            "Researched emerging AR/VR technology, and supported testing, debugging and process optimisation.",
        ],
        "tags": ["Unity", "AR/VR", "Project coordination", "Excel", "Power BI"],
        "case": "schoolvr",
    },
    {
        "role": "Unity Developer",
        "org": "Mobzway Technologies",
        "place": "Jaipur · on-site",
        "when": "Jul 2022 — Feb 2023",
        "summary": "Built 2D casino and card games for mobile in Unity and C#.",
        "stats": [],
        "bullets": [
            "Developed 2D casino game features in Unity3D (C#), optimising game loops, UI performance and cross-platform stability.",
            "Worked with artists, designers and product managers on interaction design, game flow and asset integration.",
            "Debugged, QA-tested and optimised multiple game builds, tracking outcomes in structured Excel logs.",
            "Integrated multiplayer with Socket.io and used player-behaviour data to inform feature priorities.",
        ],
        "tags": ["Unity3D", "C#", "Socket.io", "QA"],
        "case": "callbreak-multiplayer",
    },
]

SKILLS = [
    ("Business development", "How I find and win partners", [
        ("Studio &amp; publisher outreach", True), ("Lead generation", True), ("Pipeline management", True),
        ("Email, LinkedIn &amp; Discord outreach", False), ("Stakeholder communication", False),
        ("Requirement gathering", False), ("Process mapping", False), ("Playbooks &amp; documentation", False)]),
    ("Market intelligence", "How I decide who to talk to", [
        ("Steam platform research", True), ("Competitor analysis", True), ("Genre &amp; pricing trends", False),
        ("Web scraping", True), ("Lead scoring", False), ("Studio tiering", False)]),
    ("Data analytics", "How I turn data into answers", [
        ("SQL", True), ("Python", True), ("Power BI", True), ("Tableau", True), ("Advanced Excel", True),
        ("Pandas", False), ("Matplotlib &amp; Seaborn", False), ("PostgreSQL", False), ("MySQL", False),
        ("Power Query", False), ("DAX", False), ("Hypothesis testing", False), ("RFM segmentation", False)]),
    ("SQL depth", "What my queries look like", [
        ("JOINs", False), ("CTEs", False), ("Window functions", True), ("Subqueries", False), ("Aggregations", False)]),
    ("Gaming &amp; tech", "Why studios trust my read", [
        ("Unity3D", True), ("C#", False), ("AR/VR workflow", True), ("Socket.io", False), ("QA &amp; debugging", False),
        ("GitHub", False), ("Jira", False), ("Agile &amp; Scrum", False), ("Blender", False)]),
]

CERTS = [
    {"title": "Data Analyst Fellowship — Top Fellow", "by": "NextLeap · 2025", "img": "assets/img/nextleap-top-fellow.webp",
     "w": 600, "h": 759, "focus": True},
    {"title": "SQL — MySQL for Data Analytics &amp; Business Intelligence", "by": "Udemy · 365 Careers · Aug 2025",
     "img": "assets/img/udemy-sql.webp", "w": 800, "h": 595},
    {"title": "Python Bootcamp for Data Analysis &amp; Automation", "by": "Udemy"},
    {"title": "Unity 3D Game Development using C#", "by": "Udemy"},
    {"title": "C# Programming Fundamentals", "by": "Udemy"},
    {"title": "AI For Everyone", "by": "Online course"},
    {"title": "Intro to Digital Manufacturing with Autodesk Fusion 360", "by": "Online course"},
    {"title": "Materials Science: 10 Things Every Engineer Should Know", "by": "Online course"},
]

PAPER = ("Comparative Study of the Compressive Strength of Different Composites",
         "https://www.researchgate.net/publication/365248816_Comparative_Study_of_the_Compressive_Strength_of_Different_Composites")


# =====================================================================
#  SHARED LAYOUT
# =====================================================================

def asset_version(rel):
    """Short content hash so browsers fetch fresh CSS/JS after every deploy."""
    f = ROOT / rel
    return hashlib.md5(f.read_bytes()).hexdigest()[:8] if f.exists() else "0"


def page(key, path, title, desc, body, og_image="assets/img/og.png"):
    css_v = asset_version("assets/css/style.css")
    js_v = asset_version("assets/js/main.js")
    depth = path.count("/")
    r = "../" * depth
    full_title = f"{title} — {NAME}" if key != "index" else f"{NAME} — Gaming BD, Market Intelligence &amp; Data Analytics"
    nav = "\n".join(
        f'        <a href="{r}{href}"{" aria-current=\"page\"" if k == key or (key == "case" and k == "work") else ""}>{label}</a>'
        for k, href, label in NAV)
    url = SITE + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#f5f3ee" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#101216" media="(prefers-color-scheme: dark)">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}{og_image}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{r}assets/css/style.css?v={css_v}">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{r}index.html" aria-label="{NAME}, home">
        <span class="brand-mark" aria-hidden="true">YT</span>
        <span class="brand-name">{NAME}</span>
      </a>
      <button class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" class="site-nav" aria-label="Main">
{nav}
        <a href="{r}contact.html" class="nav-cta"{" aria-current=\"page\"" if key == "contact" else ""}>Contact</a>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <p class="footer-name">{NAME}</p>
        <p class="muted">Gaming BD, market intelligence &amp; data analytics. Jaipur, India — open to remote roles worldwide.</p>
      </div>
      <nav class="footer-links" aria-label="Footer">
        <a href="{r}about.html">About</a>
        <a href="{r}experience.html">Experience</a>
        <a href="{r}work.html">Work</a>
        <a href="{r}skills.html">Skills</a>
        <a href="{r}contact.html">Contact</a>
      </nav>
      <nav class="footer-links" aria-label="Elsewhere">
        <a href="mailto:{EMAIL}">Email</a>
        <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
        <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
        <a href="{r}{RESUME}" download>Résumé (PDF)</a>
      </nav>
    </div>
    <div class="wrap footer-base">
      <p>© <span data-year>2026</span> {NAME}</p>
      <a href="#top" class="to-top">Back to top ↑</a>
    </div>
  </footer>

  <dialog class="lightbox" id="lightbox" aria-label="Image preview">
    <button class="lightbox-close" aria-label="Close preview">×</button>
    <img alt="">
  </dialog>
  <script src="{r}assets/js/main.js?v={js_v}"></script>
</body>
</html>
"""


def section_head(kicker, title, lede=None, tag="h2"):
    lede_html = f'\n          <p class="section-lede">{lede}</p>' if lede else ""
    return f"""        <header class="section-head">
          <p class="kicker mono">{kicker}</p>
          <{tag}>{title}</{tag}>{lede_html}
        </header>"""


def chips(items, hi=()):
    return '<ul class="chips">' + "".join(
        f'<li{" class=\"hi\"" if i in hi else ""}>{i}</li>' for i in items) + "</ul>"


def thumb(p, r):
    t = p["thumb"]
    if t["type"] == "img":
        return (f'<img src="{r}{t["src"]}" alt="" width="{t["w"]}" height="{t["h"]}" loading="lazy">')
    if t["type"] == "code":
        lines = "".join(f"<span>{escape(l)}</span>" for l in t["lines"])
        return f'<div class="thumb-code mono" aria-hidden="true">{lines}</div>'
    if t["type"] == "funnel":
        return """<div class="thumb-funnel" aria-hidden="true">
              <span style="--w:100%">500+ titles</span><span style="--w:74%">100+ studios</span>
              <span style="--w:48%">30%+ reply</span><span style="--w:24%">1 deal</span></div>"""
    return f'<div class="thumb-glyph" aria-hidden="true"><span>{t["label"]}</span></div>'


def project_card(p, r, big=False):
    return f"""          <a class="card{" card-big" if big else ""}" href="{r}work/{p['slug']}.html" data-cat="{p['cat']}">
            <div class="card-thumb">{thumb(p, r)}</div>
            <div class="card-body">
              <p class="card-cat mono">{CATS[p['cat']]}</p>
              <h3>{p['short']}</h3>
              <p>{p['card']}</p>
              <p class="card-tools mono">{" · ".join(p['tools'][:4])}</p>
            </div>
          </a>"""


CAREER_SVG = """<svg viewBox="0 0 420 260" role="img" aria-label="Career path: B.Tech Mechanical Engineering 2018 to 2022, Unity Developer 2022, AR/VR Executive 2023 to 2025, NextLeap Data Analyst Fellowship 2025, BD and Outreach Specialist at Brothers Interactive from October 2025.">
            <g class="grid"><line x1="40" y1="40" x2="400" y2="40"/><line x1="40" y1="95" x2="400" y2="95"/><line x1="40" y1="150" x2="400" y2="150"/><line x1="40" y1="205" x2="400" y2="205"/></g>
            <g class="axis mono"><text x="40" y="238">2018</text><text x="160" y="238">2022</text><text x="250" y="238">2023</text><text x="325" y="238">2025</text><text x="400" y="238" text-anchor="end">now</text></g>
            <path class="area" d="M40,205 L160,205 L160,160 L250,160 L250,118 L325,118 L325,82 L360,82 L360,48 L400,48 L400,220 L40,220 Z"/>
            <path class="line" d="M40,205 L160,205 L160,160 L250,160 L250,118 L325,118 L325,82 L360,82 L360,48 L400,48"/>
            <g class="points"><circle cx="100" cy="205" r="4"/><circle cx="205" cy="160" r="4"/><circle cx="287" cy="118" r="4"/><circle cx="342" cy="82" r="4"/><circle class="now" cx="380" cy="48" r="6"/></g>
            <g class="labels"><text x="100" y="193" text-anchor="middle">B.Tech, Mech. Eng.</text><text x="205" y="148" text-anchor="middle">Unity Dev</text><text x="287" y="106" text-anchor="middle">AR/VR Exec</text><text x="332" y="70" text-anchor="end">Data Fellow</text><text class="strong" x="392" y="30" text-anchor="end">Gaming BD + Data</text></g>
          </svg>"""


# =====================================================================
#  PAGES
# =====================================================================

def home():
    r = ""
    featured = [p for p in PROJECTS if p["slug"] in (
        "visa-transaction-analysis", "flipkart-customer-service", "madhav-ecommerce-dashboard",
        "pizza-sales-sql", "airbnb-sql-analysis", "schoolvr")]
    steam = PROJECTS[0]
    body = f"""    <section class="hero" id="top">
      <div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div>
      <div class="wrap">
        <p class="eyebrow"><span class="dot" aria-hidden="true"></span> Open to remote Gaming BD, market research &amp; analyst roles</p>
        <h1 class="display">I help game studios find the right partners — <em>with data.</em></h1>
        <div class="hero-row">
          <p class="lede">
            I'm Yogesh. I built games in Unity and ran AR/VR projects before moving into analytics. Now I do business
            development and market intelligence at Brothers Interactive — scraping Steam, scoring studios in Python and
            SQL, and writing outreach people actually answer.
          </p>
          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="work.html">See my work</a>
            <a class="btn btn-ghost btn-lg" href="{RESUME}" download>Download résumé</a>
          </div>
        </div>
      </div>

      <div class="wrap">
        <div class="board">
          <figure class="board-card board-funnel" aria-labelledby="funnel-cap">
            <figcaption id="funnel-cap" class="chart-title"><span>Outreach funnel</span><span class="mono muted">Brothers Interactive · Oct 2025 → now</span></figcaption>
            <div class="viz-bars" role="img" aria-label="Funnel: 500+ Steam titles analysed, studios tiered by fit, 100+ contacted, 30%+ replied, 1 partnership signed.">
              <div class="viz-bar" style="--h:100%"><b class="mono">500+</b><i></i><span>titles</span></div>
              <div class="viz-bar" style="--h:80%"><b class="mono">Tier</b><i></i><span>scored</span></div>
              <div class="viz-bar" style="--h:62%"><b class="mono">100+</b><i></i><span>contacted</span></div>
              <div class="viz-bar" style="--h:44%"><b class="mono">30%+</b><i></i><span>replied</span></div>
              <div class="viz-bar is-win" style="--h:26%"><b class="mono">1</b><i></i><span>signed</span></div>
            </div>
          </figure>

          <figure class="board-card board-gauge" aria-labelledby="gauge-cap">
            <figcaption id="gauge-cap" class="chart-title"><span>Reply rate</span><span class="mono muted">vs industry</span></figcaption>
            <div class="gauge" role="img" aria-label="My outreach reply rate is over 30 percent; the industry average is 5 to 10 percent.">
              <svg viewBox="0 0 140 140">
                <circle class="gauge-track" cx="70" cy="70" r="58"/>
                <circle class="gauge-ind" cx="70" cy="70" r="58" pathLength="100" stroke-dasharray="7.5 92.5"/>
                <circle class="gauge-me" cx="70" cy="70" r="58" pathLength="100" stroke-dasharray="30 70"/>
              </svg>
              <div class="gauge-center"><b class="mono" data-count="30" data-suffix="%+">30%+</b><span>mine</span></div>
            </div>
            <p class="gauge-foot"><span class="swatch swatch-ind"></span>Industry 5–10% <span class="swatch swatch-me"></span>Me 30%+</p>
          </figure>

          <dl class="board-card board-kpis">
            <div><dd class="mono" data-count="500" data-suffix="+">500+</dd><dt>Steam titles scraped &amp; analysed</dt></div>
            <div><dd class="mono" data-count="100" data-suffix="+">100+</dd><dt>Studios &amp; publishers contacted</dt></div>
            <div><dd class="mono" data-count="1310" data-suffix="">1,310</dd><dt>Lines of Python in my Steam scraper</dt></div>
            <div><dd class="mono">Top Fellow</dd><dt>NextLeap Data Analyst Fellowship, 2025</dt></div>
          </dl>
        </div>
      </div>
    </section>

    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">
        <span>Python</span><span>SQL</span><span>Power BI</span><span>Tableau</span><span>Advanced Excel</span><span>Steam research</span><span>Pandas</span><span>PostgreSQL</span><span>Web scraping</span><span>Unity3D</span><span>Lead scoring</span><span>Studio outreach</span>
        <span>Python</span><span>SQL</span><span>Power BI</span><span>Tableau</span><span>Advanced Excel</span><span>Steam research</span><span>Pandas</span><span>PostgreSQL</span><span>Web scraping</span><span>Unity3D</span><span>Lead scoring</span><span>Studio outreach</span>
      </div>
    </div>

    <section class="section section-alt">
      <div class="wrap">
{section_head("What I do", "Three skills that rarely come in one person", "Most BD people can't write SQL. Most analysts have never shipped a game. I've done all three jobs, so each one makes the others better.")}
        <div class="pillars">
          <article class="pillar">
            <span class="pillar-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5M8 13v-3M11 13V8M14 13v-2"/></svg></span><span class="pillar-num mono">01</span>
            <h3>Market intelligence</h3>
            <p>I scrape and analyse Steam — genres, pricing, review trends, publisher activity — to find the studios worth talking to, and the reason they'd want to talk back.</p>
            <a class="link-arrow" href="work/steam-market-intelligence.html">Steam research case study</a>
          </article>
          <article class="pillar">
            <span class="pillar-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 3 10 14M21 3l-7 18-4-8-8-4 18-7Z"/></svg></span><span class="pillar-num mono">02</span>
            <h3>Business development</h3>
            <p>Research-first outreach across email, LinkedIn and Discord, a scored lead pipeline, and playbooks the team can reuse. 100+ studios contacted, one partnership signed.</p>
            <a class="link-arrow" href="experience.html">What I do at Brothers Interactive</a>
          </article>
          <article class="pillar">
            <span class="pillar-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></svg></span><span class="pillar-num mono">03</span>
            <h3>Data analytics</h3>
            <p>SQL, Python, Power BI, Tableau and Excel — from hypothesis tests on 1.3M transactions to dashboards managers use every week.</p>
            <a class="link-arrow" href="work.html">Dashboards &amp; SQL work</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
{section_head("Featured case study", "From 500 Steam pages to a signed studio partnership")}
        <div class="feature">
          <div class="scrape-panel">
            <div class="scrape-head mono"><span class="scrape-dots" aria-hidden="true"><i></i><i></i><i></i></span>steam_research.py · 1,310 lines</div>
            <table class="scrape-table mono">
              <thead><tr><th>field</th><th>what it tells me</th></tr></thead>
              <tbody>
                <tr><td>genre, tags</td><td>does their pipeline match what we make</td></tr>
                <tr><td>price, discounts</td><td>budget tier of the studio</td></tr>
                <tr><td>reviews / month</td><td>is the game growing or fading</td></tr>
                <tr><td>publisher activity</td><td>who really signs the contract</td></tr>
                <tr><td>socials, discord</td><td>the channel they actually answer</td></tr>
                <tr class="scrape-out"><td>→ lead_score</td><td>tier A / B / C, then outreach</td></tr>
              </tbody>
            </table>
          </div>
          <div class="feature-copy">
            <p>{steam['question']}</p>
            <p>I wrote a 1,310-line Python scraper, turned the output into a lead-scoring model, and built outreach around what each studio was actually shipping.</p>
            <a class="btn btn-primary" href="work/{steam['slug']}.html">Read the case study</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <div class="head-row">
{section_head("Selected work", "Dashboards, SQL and things I've built")}
          <a class="link-arrow" href="work.html">All {len(PROJECTS)} projects</a>
        </div>
        <div class="card-grid">
{chr(10).join(project_card(p, r) for p in featured)}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
{section_head("Background", "Engineer → game developer → XR → data → gaming BD", "Each move added a layer: engineering taught me systems, games taught me players, XR taught me clients, data taught me proof — and BD is where they all pay off.")}
          <div class="hero-actions">
            <a class="btn btn-ghost" href="about.html">My story</a>
            <a class="btn btn-ghost" href="experience.html">Full experience</a>
          </div>
        </div>
        <figure class="career-chart" aria-labelledby="career-cap">
          <figcaption id="career-cap" class="chart-title"><span>Career, plotted</span><span class="mono muted">2018 → today</span></figcaption>
          {CAREER_SVG}
        </figure>
      </div>
    </section>
{cta_band(r)}"""
    return page("index", "index.html", NAME,
                "Yogesh Tiwari helps game studios find the right partners with data — Steam market intelligence, "
                "business development and analytics in SQL, Python, Power BI and Tableau. Jaipur, India.", body)


def cta_band(r):
    return f"""    <section class="cta-band">
      <div class="wrap cta-inner">
        <div>
          <h2>Working in gaming? Let's talk.</h2>
          <p>Open to remote Gaming BD, market research and business analyst roles — and to studios looking for partners.</p>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{r}contact.html">Get in touch</a>
          <a class="btn btn-ghost-inv" href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
    </section>"""


def about():
    body = f"""    <section class="page-hero" id="top">
      <div class="wrap">
        <p class="kicker mono">About</p>
        <h1>I sit where gaming, data and business development meet.</h1>
        <p class="lede">That's a rare mix, and it's the whole point. I understand what game developers need because I've been one — and I can back every outreach decision with data.</p>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap split split-start">
        <div class="prose">
          <h2>The short version</h2>
          <p>I trained as a mechanical engineer at Rajkiya Engineering College, Mainpuri, and graduated in 2022. Curiosity about how things work pulled me toward software, and my first job was building 2D casino and card games in Unity at Mobzway Technologies. Writing gameplay logic taught me to think clearly and debug patiently.</p>
          <p>From there I moved into AR/VR at the Atal Incubation Centre, Manipal University Jaipur. For two years I led immersive projects for 5+ startup partners, ran strategy workshops with founders, and mentored junior developers. That's where I saw how much stronger a product becomes when it's tied to real business needs — and how much of that comes down to data.</p>
          <p>So I went deep on analytics. The NextLeap Data Analyst Fellowship put me through real business cases in SQL, Python, Tableau and Power BI, and I graduated as a Top Fellow in 2025.</p>
          <p>Today, at Brothers Interactive, all of it comes together. I research the Steam market with my own Python tools, score and tier studios, and run business development with game studios and publishers worldwide. My outreach gets a 30%+ reply rate — 3–5× the industry norm — because I speak to studios as someone who has shipped games.</p>
        </div>
        <figure class="career-chart sticky-head" aria-labelledby="career-cap">
          <figcaption id="career-cap" class="chart-title"><span>Career, plotted</span><span class="mono muted">2018 → today</span></figcaption>
          {CAREER_SVG}
        </figure>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
{section_head("How I work", "Four habits I bring to every role")}
        <div class="pillars pillars-4">
          <article class="pillar"><span class="pillar-num mono">01</span><h3>Research before reach-out</h3><p>No message goes out until I know the studio's games, audience and market position. It's why people reply.</p></article>
          <article class="pillar"><span class="pillar-num mono">02</span><h3>Question first, tool second</h3><p>I start from the decision someone needs to make, then pick SQL, Python or a dashboard — not the other way round.</p></article>
          <article class="pillar"><span class="pillar-num mono">03</span><h3>Speak both languages</h3><p>I've been the developer and the business person, so I can translate between studios, sales and engineering without losing detail.</p></article>
          <article class="pillar"><span class="pillar-num mono">04</span><h3>Make it repeatable</h3><p>Scrapers, scoring sheets, playbooks and templates — I document the process so the next result doesn't depend on me.</p></article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split split-start">
        <div>
{section_head("Education", "B.Tech, Mechanical Engineering")}
          <div class="prose">
            <p><strong>Rajkiya Engineering College, Mainpuri</strong> — affiliated with AKTU, Lucknow. August 2018 to July 2022, graduated with 77.5%.</p>
            <p>Focused on mechanical systems, product design and data-driven methods, and published a conference paper comparing the compressive strength of composite materials.</p>
            <a class="link-arrow" href="{PAPER[1]}" target="_blank" rel="noopener">Read the paper on ResearchGate</a>
          </div>
        </div>
        <div>
{section_head("Outside work", "What keeps me curious")}
          <div class="prose">
            <p>Games — as a player and as someone who reads Steam charts for fun. Sports analytics, especially cricket. And emerging tech: I still follow what's happening in XR and AI, and how studios are using both.</p>
            <a class="link-arrow" href="skills.html">Skills &amp; certifications</a>
          </div>
        </div>
      </div>
    </section>
{cta_band("")}"""
    return page("about", "about.html", "About",
                "Mechanical engineer turned Unity developer, AR/VR executive, data analyst and gaming BD specialist — "
                "Yogesh Tiwari's story.", body)


def experience():
    items = []
    for e in EXPERIENCE:
        stats = ""
        if e["stats"]:
            stats = '<dl class="exp-stats">' + "".join(
                f"<div><dd class=\"mono\">{v}</dd><dt>{k}</dt></div>" for v, k in e["stats"]) + "</dl>"
        org = e["org"] + (f' <span class="muted">({e["orgfull"]})</span>' if e.get("orgfull") else "")
        case = next(p for p in PROJECTS if p["slug"] == e["case"])
        items.append(f"""          <li class="exp">
            <div class="exp-side">
              <p class="when mono">{e['when']}</p>
              <p class="muted small">{e['place']}</p>
            </div>
            <div class="exp-main">
              <h2>{e['role']}</h2>
              <p class="exp-org">{org}</p>
              <p class="exp-summary">{e['summary']}</p>
              {stats}
              <ul class="bullets">
                {"".join(f"<li>{b}</li>" for b in e['bullets'])}
              </ul>
              {chips(e['tags'])}
              <a class="link-arrow" href="work/{case['slug']}.html">Related: {case['short']}</a>
            </div>
          </li>""")
    body = f"""    <section class="page-hero" id="top">
      <div class="wrap">
        <p class="kicker mono">Experience</p>
        <h1>Four years across games, XR, data and business development.</h1>
        <p class="lede">Every role below built on the last. The numbers are real, and each role links to a project from that time.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{RESUME}" download>Download résumé (PDF)</a>
          <a class="btn btn-ghost" href="{LINKEDIN}" target="_blank" rel="noopener">View on LinkedIn</a>
        </div>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap">
        <ol class="exp-list">
{chr(10).join(items)}
          <li class="exp exp-edu">
            <div class="exp-side">
              <p class="when mono">2018 — 2022</p>
              <p class="muted small">Mainpuri, UP</p>
            </div>
            <div class="exp-main">
              <h2>B.Tech, Mechanical Engineering</h2>
              <p class="exp-org">Rajkiya Engineering College, Mainpuri <span class="muted">(AKTU, Lucknow)</span></p>
              <p class="exp-summary">Graduated with 77.5%. Published a conference paper on the compressive strength of composite materials.</p>
            </div>
          </li>
        </ol>
      </div>
    </section>
{cta_band("")}"""
    return page("experience", "experience.html", "Experience",
                "Yogesh Tiwari's experience: BD & Outreach Specialist at Brothers Interactive, NextLeap Data Analyst "
                "Fellow, AR/VR Executive at AICMUJ, and Unity Developer at Mobzway.", body)


def work():
    filters = "".join(
        f'<button class="filter" data-filter="{k}" aria-pressed="false">{v} <span class="mono">{sum(p["cat"] == k for p in PROJECTS)}</span></button>'
        for k, v in CATS.items())
    body = f"""    <section class="page-hero" id="top">
      <div class="wrap">
        <p class="kicker mono">Work</p>
        <h1>Projects &amp; case studies</h1>
        <p class="lede">Market research, dashboards, SQL analysis and the games and XR products I built before. Each one starts with a real question and ends with what I'd do about the answer.</p>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap">
        <div class="filters" role="group" aria-label="Filter projects">
          <button class="filter" data-filter="all" aria-pressed="true">All <span class="mono">{len(PROJECTS)}</span></button>
          {filters}
        </div>
        <div class="card-grid" id="project-grid">
{chr(10).join(project_card(p, "") for p in PROJECTS)}
        </div>
        <p class="grid-note muted">More on <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>, including the raw data and queries behind these projects.</p>
      </div>
    </section>
{cta_band("")}"""
    return page("work", "work.html", "Work",
                "Case studies by Yogesh Tiwari: Steam market intelligence, Visa, Flipkart and e-commerce dashboards, "
                "SQL analyses, and Unity/VR builds.", body)


def case(i):
    p = PROJECTS[i]
    r = "../"
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    t = p["thumb"]
    if t["type"] == "img":
        visual = f"""        <button class="case-hero-img" data-full="{r}{t['src']}" aria-label="Enlarge the dashboard">
          <img src="{r}{t['src']}" alt="{p['short']} dashboard" width="{t['w']}" height="{t['h']}">
        </button>"""
    elif p.get("code"):
        visual = f"""        <pre class="code code-hero"><code class="sql">{escape(p['code'])}</code></pre>"""
    elif t["type"] == "funnel":
        visual = """        <ol class="funnel funnel-wide" aria-label="Outreach funnel">
          <li style="--w:100%"><span class="mono">500+</span> Steam titles scraped &amp; analysed</li>
          <li style="--w:82%"><span class="mono">Tiered</span> studios scored by fit</li>
          <li style="--w:64%"><span class="mono">100+</span> studios &amp; publishers contacted</li>
          <li style="--w:46%"><span class="mono">30%+</span> replied — 3–5× industry</li>
          <li style="--w:28%" class="is-win"><span class="mono">1</span> partnership signed</li>
        </ol>"""
    else:
        visual = f'        <div class="glyph-hero" aria-hidden="true"><span>{t["label"]}</span></div>'

    figures = "".join(f"<div><dd class=\"mono\">{v}</dd><dt>{k}</dt></div>" for v, k in p["figures"])
    steps = "".join(
        f'<li><span class="step-n mono">{n:02d}</span><div><h3>{a}</h3><p>{b}</p></div></li>'
        for n, (a, b) in enumerate(p["approach"], 1))
    findings = "".join(f"<li>{f}</li>" for f in p["findings"])
    recommend = ""
    if p.get("recommend"):
        recommend = f"""
          <h2>What I'd recommend</h2>
          <ul class="bullets">{"".join(f"<li>{x}</li>" for x in p["recommend"])}</ul>"""
    code_block = ""
    if p.get("code") and t["type"] == "img":
        code_block = f'<pre class="code"><code class="sql">{escape(p["code"])}</code></pre>'
    note = f'<p class="case-note muted">{p["note"]}</p>' if p.get("note") else ""
    links = "".join(
        f'<a class="btn btn-ghost" href="{u}" target="_blank" rel="noopener">{l} ↗</a>' for l, u in p["links"])
    links_block = f'<div class="hero-actions">{links}</div>' if links else ""

    body = f"""    <section class="page-hero case-hero" id="top">
      <div class="wrap">
        <nav class="crumbs mono" aria-label="Breadcrumb"><a href="{r}work.html">Work</a> <span aria-hidden="true">/</span> {CATS[p['cat']]}</nav>
        <h1>{p['title']}</h1>
        <dl class="case-facts">
          <div><dt>Role</dt><dd>{p['role']}</dd></div>
          <div><dt>When</dt><dd>{p['when']}</dd></div>
          <div><dt>Tools</dt><dd>{" · ".join(p['tools'])}</dd></div>
        </dl>
        {links_block}
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap">
{visual}
        <dl class="case-figures">{figures}</dl>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap case-layout">
        <aside class="case-toc" aria-label="On this page">
          <p class="mono muted">On this page</p>
          <a href="#question">The question</a><a href="#data">The data</a><a href="#approach">Approach</a><a href="#findings">Findings</a>
        </aside>
        <article class="prose case-prose">
          <h2 id="question">The question</h2>
          <p>{p['question']}</p>
          <h2 id="data">The data</h2>
          <p>{p['data']}</p>
          <h2 id="approach">Approach</h2>
          <ol class="steps">{steps}</ol>
          {code_block}
          <h2 id="findings">What I found</h2>
          <ul class="bullets">{findings}</ul>{recommend}
          {note}
        </article>
      </div>
    </section>

    <nav class="case-nav wrap" aria-label="More projects">
      <a href="{r}work/{prev_p['slug']}.html"><span class="mono muted">← Previous</span>{prev_p['short']}</a>
      <a href="{r}work/{next_p['slug']}.html" class="next"><span class="mono muted">Next →</span>{next_p['short']}</a>
    </nav>
{cta_band(r)}"""
    desc = f"{p['card']} A case study by {NAME}."
    og = t["src"] if t["type"] == "img" else "assets/img/og.png"
    return page("case", f"work/{p['slug']}.html", p["short"], escape(desc, quote=True).replace("&amp;amp;", "&amp;"),
                body, og_image=og)


def skills():
    groups = "".join(f"""
          <div class="skill-group">
            <h2>{g}</h2>
            <p class="muted">{sub}</p>
            {chips([s for s, _ in items], hi=[s for s, h in items if h])}
          </div>""" for g, sub, items in SKILLS)
    certs = []
    for c in CERTS:
        if c.get("img"):
            focus = ' class="focus-center"' if c.get("focus") else ""
            certs.append(f"""          <button class="cert" data-full="{c['img']}" aria-label="Enlarge certificate: {c['title']}">
            <img{focus} src="{c['img']}" alt="Certificate: {c['title']}" width="{c['w']}" height="{c['h']}" loading="lazy">
            <span class="cert-text"><strong>{c['title']}</strong><span class="muted">{c['by']}</span></span>
          </button>""")
        else:
            certs.append(f"""          <div class="cert cert-plain">
            <span class="cert-text"><strong>{c['title']}</strong><span class="muted">{c['by']}</span></span>
          </div>""")
    body = f"""    <section class="page-hero" id="top">
      <div class="wrap">
        <p class="kicker mono">Skills</p>
        <h1>Toolkit &amp; certifications</h1>
        <p class="lede">Grouped by what I use them for. Highlighted skills are the ones I use every week.</p>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap skills skills-page">{groups}
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
{section_head("Certifications", "Courses, fellowship &amp; publication")}
        <div class="cert-grid">
{chr(10).join(certs)}
          <a class="cert cert-plain cert-paper-link" href="{PAPER[1]}" target="_blank" rel="noopener">
            <span class="cert-text"><span class="mono kicker">Publication</span><strong>{PAPER[0]}</strong><span class="muted">Conference paper · ResearchGate ↗</span></span>
          </a>
        </div>
      </div>
    </section>
{cta_band("")}"""
    return page("skills", "skills.html", "Skills",
                "Yogesh Tiwari's toolkit: business development, Steam market intelligence, SQL, Python, Power BI, "
                "Tableau, Excel, Unity — plus certifications.", body)


def contact():
    body = f"""    <section class="page-hero" id="top">
      <div class="wrap">
        <p class="kicker mono">Contact</p>
        <h1>Let's talk.</h1>
        <p class="lede">I'm open to remote Gaming BD, market research and business analyst roles worldwide — and always happy to hear from studios and people in games.</p>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap contact-grid">
        <div class="contact-direct">
          <h2>Reach me directly</h2>
          <ul class="contact-list">
            <li><span class="mono muted">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><span class="mono muted">LinkedIn</span><a href="{LINKEDIN}" target="_blank" rel="noopener">in/yogesh-tiwari2000</a></li>
            <li><span class="mono muted">GitHub</span><a href="{GITHUB}" target="_blank" rel="noopener">TiwariYogi2001</a></li>
            <li><span class="mono muted">WhatsApp</span><a href="{WHATSAPP}" target="_blank" rel="noopener">Message me</a></li>
            <li><span class="mono muted">Based in</span><span>Jaipur, India · IST (UTC+5:30)</span></li>
          </ul>
          <a class="btn btn-ghost" href="{RESUME}" download>Download résumé (PDF)</a>
        </div>

        <form class="contact-form" id="contact-form" novalidate>
          <h2>Or send a message</h2>
          <input type="text" name="_honey" id="honey" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
          <div class="field">
            <label for="name">Name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="subject">Subject</label>
            <input id="subject" name="subject" type="text" required>
          </div>
          <div class="field">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="6" required></textarea>
          </div>
          <button class="btn btn-primary" type="submit">Send message</button>
          <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>"""
    return page("contact", "contact.html", "Contact",
                f"Contact Yogesh Tiwari — open to remote Gaming BD, market research and business analyst roles. {EMAIL}",
                body)


def not_found():
    body = """    <section class="page-hero page-404" id="top">
      <div class="wrap">
        <p class="kicker mono">404 — not found</p>
        <h1>That page isn't in the dataset.</h1>
        <p class="lede">The link may be old, or the page may have moved.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/website/index.html">Go to the homepage</a>
          <a class="btn btn-ghost" href="/website/work.html">See my work</a>
        </div>
      </div>
    </section>"""
    html = page("404", "404.html", "Page not found", "This page could not be found.", body)
    # 404.html is served from any path, so point shared assets at the site root.
    return html.replace('href="assets/', 'href="/website/assets/').replace('src="assets/', 'src="/website/assets/') \
               .replace('href="index.html"', 'href="/website/index.html"') \
               .replace('href="about.html"', 'href="/website/about.html"') \
               .replace('href="experience.html"', 'href="/website/experience.html"') \
               .replace('href="work.html"', 'href="/website/work.html"') \
               .replace('href="skills.html"', 'href="/website/skills.html"') \
               .replace('href="contact.html"', 'href="/website/contact.html"')


# =====================================================================
#  BUILD
# =====================================================================

def main():
    out = {
        "index.html": home(),
        "about.html": about(),
        "experience.html": experience(),
        "work.html": work(),
        "skills.html": skills(),
        "contact.html": contact(),
        "404.html": not_found(),
    }
    for i, p in enumerate(PROJECTS):
        out[f"work/{p['slug']}.html"] = case(i)

    for path, html in out.items():
        f = ROOT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8", newline="\n")

    urls = [u for u in out if u != "404.html"]
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{SITE}{'' if u == 'index.html' else u}</loc></url>\n" for u in urls) +
        "</urlset>\n", encoding="utf-8", newline="\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n",
                                     encoding="utf-8", newline="\n")
    print(f"Built {len(out)} pages.")


if __name__ == "__main__":
    main()
