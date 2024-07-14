# import lightningchart as lc
# import pandas as pd
# import numpy as np
# import time

# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Navigation/output.csv'
# df = pd.read_csv(file_path)

# df['time_ms'] = df['sample_number'] * df['sample_interval_in_ms_for_this_trace'] / 1000.0

# chart = lc.ChartXY(
#     theme=lc.Themes.Dark,
#     title='Real-Time Seismic Trace Display'
# )
# chart.set_animations_enabled(False)
# series = chart.add_line_series()

# chart.get_default_x_axis().set_title('Time (ms)')
# chart.get_default_y_axis().set_title('Amplitude')

# chart.open(live=True)

# def update_chart(trace_number):
#     trace_data = df[df['trace_sequence_number_within_line'] == trace_number]
#     if not trace_data.empty:
#         x_values = trace_data['time_ms'].values.tolist()
#         y_values = trace_data['trace_value'].values.tolist()
#         series.clear().add(x_values, y_values)
#         chart.set_title(f'Real-Time Seismic Trace Display - Trace {trace_number}')

# for trace_number in df['trace_sequence_number_within_line'].unique():
#     update_chart(trace_number)
#     time.sleep(1.0)  

# chart.close()



import lightningchart as lc
import pandas as pd
import time

with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/Blake_Ridge_Hydrates_3D/Export/Steering_background.csv'
df = pd.read_csv(file_path)

df['time_ms'] = df['sample_number'] * df['sample_interval_in_ms_for_this_trace'] / 1000.0

dashboard = lc.Dashboard(columns=2, rows=3, theme=lc.Themes.Dark)

chart1 = dashboard.ChartXY(column_index=0, row_index=0, column_span=2, row_span=2)
series1 = chart1.add_line_series(data_pattern='ProgressiveX')

x_axis = chart1.get_default_x_axis()
x_axis.set_scroll_strategy(strategy='progressive')
x_axis.set_interval(start=-500, end=0, stop_axis_after=False)
chart1.get_default_y_axis().set_title('Amplitude')
chart1.set_title('Real-Time Seismic Trace Display')

zbc = dashboard.ZoomBandChart(chart=chart1, column_index=0, row_index=2, column_span=2, row_span=1)
zbc.add_series(series1)

dashboard.open(live=True)

def update_chart(trace_number):
    trace_data = df[df['trace_sequence_number_within_segy_file'] == trace_number]
    if not trace_data.empty:
        x_values = trace_data['time_ms'].values.tolist()
        y_values = trace_data['trace_value'].values.tolist()
        series1.clear().add(x_values, y_values)
        chart1.set_title(f'Real-Time Seismic Trace Display - Trace {trace_number}')

for trace_number in df['trace_sequence_number_within_segy_file'].unique():
    update_chart(trace_number)
    time.sleep(1.0)

dashboard.close()
