import plotly.io as pio

#Рендерер
pio.renderers.default = "png"
pio.kaleido.scope.default_scale = 2

#Цветовая палитра
PRIMARY = "#404040"
PRIMARY_DARK = "#4A4A4A"
PRIMARY_LIGHT = "#8A8A8A"
PRIMARY_VERY_LIGHT = "#D9D9D9"

ACCENT = "#8C8C8C"
ACCENT_DARK = "#666666"
ACCENT_LIGHT = "#CFCFCF"

NEUTRAL = "#7A7A7A"

AXIS_COLOR = "#666666"
GRID_COLOR = "#E3E3E3"


def apply_layout(fig, *, width=900, height=500, font_size=14,
                 x_title="", y_title="", y_max=None,
                 margin_b=80, margin_l=60, margin_r=60, margin_t=40,
                 tickangle=0, show_legend=False):
    
    layout = dict(
        showlegend=show_legend,
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Times New Roman", size=font_size, color="#000000"),
        xaxis=dict(
            title=x_title,
            showgrid=False,
            tickfont=dict(size=font_size),
            linecolor=AXIS_COLOR,
            linewidth=1,
            tickangle=tickangle,
        ),
        yaxis=dict(
            title=y_title,
            titlefont=dict(size=font_size + 1),
            tickfont=dict(size=font_size),
            showgrid=True,
            gridcolor=GRID_COLOR,
            zeroline=False,
            linecolor=AXIS_COLOR,
            linewidth=1,
        ),
        margin=dict(l=margin_l, r=margin_r, t=margin_t, b=margin_b),
        width=width,
        height=height,
    )
    if y_max is not None:
        layout["yaxis"]["range"] = [0, y_max]
    fig.update_layout(**layout)
    return fig
