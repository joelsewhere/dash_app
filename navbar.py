import dash_bootstrap_components as dbc


def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Menu",
                 children=[
                    dbc.DropdownMenuItem("Entry 1"),
                    dbc.DropdownMenuItem("Entry 2"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Entry 3"),
                          ],
                      ),
                    ],
          brand="Home",
          brand_href="/home",
          sticky="top",
        )
     return navbar
