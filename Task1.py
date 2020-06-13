from solid import *
from solid.utils import *

heig = 2.5

low1_c = color('DarkGoldenrod')(up(heig)(cylinder(r=8, h=2)))
low_c = color('DarkGoldenrod')(cylinder(r=10, h=heig))

tube = color('Goldenrod')(up(heig+2)(cylinder(r=6, h=45)))

up1_c = color('Goldenrod')(up(heig+47)(cylinder(r=8, h=2)))
up_c = color('Goldenrod')(up(heig+49)(cylinder(r=10, h=heig)))

cuz = 2*heig+49+5

up_ex1 = circle(r=1)
for i in range(0, 181, 90):
    up_ex1 += color('SandyBrown')(up(cuz)(linear_extrude(
        height=10, center=True, convexity=10, twist=-360)(
            arc_inverted(rad=7, start_degrees=i, end_degrees=i+90))))

up_ex11 = circle(r=1)
for i in range(0, 181, 90):
    up_ex11 += color('SandyBrown')(up(cuz)(linear_extrude(
        height=10, center=True, convexity=10, twist=360)(
            arc_inverted(rad=7, start_degrees=i, end_degrees=i+90))))

# up_ex1 += up_ex11

col = low1_c + low_c + tube + up_c + up1_c + up_ex1

col_1 = right(36)(col)
col_2 = right(12)(col)
col_3 = left(12)(col)
col_4 = left(36)(col)

text = right(50)(text("Oscar Awards", 10, "Arial:style=Black"))
text += color('Crimson')(text)

result = col_1 + col_2 + col_3 + col_4 + text

scad_render_to_file(result)
