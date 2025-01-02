import numpy as np
import plotly.graph_objects as go

vector1 = np.array([3, 5, 1])
vector2 = np.array([0, 2, 2])
vector_list = np.random.uniform(-4, 4, (100, 2))
vector_space = [vector1 * scalars[0] + vector2 * scalars[1] for scalars in vector_list]
vector_space = np.array(vector_space)
fig = go.Figure()
fig.add_trace(go.Scatter3d(x=vector_space[:, 0], y=vector_space[:, 1], z=vector_space[:, 2], mode='markers'))
fig.show(renderer="browser")