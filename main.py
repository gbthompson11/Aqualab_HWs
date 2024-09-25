import plotly.express as px

test_x = ['a', 'b', 'c', 'd', 'e']
test_y = [6, 1, 4, 9, 11]

fig = px.bar(title="Aqualab Graph Proof of Concept", x=test_x, y=test_y)
fig.write_html("html_1.html", auto_open=True)
