from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=select_autoescape()
)
#  starting requisition
requisition = 10
#  team size
requisition += (team_size if team_size > 5 else 5) * 2
#  clearance level
requisition += (clearance - 1) * 2
#  seniority
requisition += round_down(avg_lvl / 2)
#  case file threat
requisition += threat
#  good books
requisition += 1 if good_books else 0
#  blacklist
blacklist_lvl
