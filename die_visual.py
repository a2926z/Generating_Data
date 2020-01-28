from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
roll_times = 1000000
for roll_num in range(roll_times):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

Perc = []
for xyz in frequencies:
    perc = (xyz/sum(frequencies))*100
    Perc.append(perc)
    print(perc.__round__(2))

# Visualize the results.
x_values = list(range(2, max_result+1))
y_result = Perc #or frequencies
data = [Bar(x=x_values, y=y_result)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': ('Frequency of rolling ' + str(roll_times) + ' times')}

my_layout = Layout(title='Results of rolling two D6 ' + str(roll_times) + ' times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

print(results)
print(frequencies)
