w, h = 1000, 1000

min_lines = 4
max_lines = 9
curved_runes = True
grid_pixel_width = 900
grid_pixel_height = 900
grid_width = 60
grid_height = 60

rune_width = 10
rune_height = 10

noise_scale = .02

# position, grid width, grid height, pixel width, pixel height, line weight
def draw_rune(x, y, gw, gh, pw, ph, lw):
    horizontal_point_sep = float(pw)/(gw - 1)
    vertical_point_sep = float(ph)/(gh - 1)
    
    rune_point = (x - pw/2.0, y - ph/2.0)
    
    rune_points = []
    for r in range(gh):
        for c in range(gw):
            rune_points.append(rune_point)
            
            rune_point = (rune_point[0] + horizontal_point_sep, rune_point[1])
        rune_point = (x - pw/2.0, rune_point[1] + vertical_point_sep)
    
    current_point = rune_points[int(random(len(rune_points)))]
    
    if (not curved_runes):
        for i in range(int(random(min_lines, max_lines))):
            next_point = rune_points[int(random(len(rune_points)))]
            line(current_point[0], current_point[1], next_point[0], next_point[1])
            
            current_point = next_point
    else:
        beginShape();
        for i in range(int(random(min_lines, max_lines))):
            curveVertex(current_point[0], current_point[1]);
            current_point = rune_points[int(random(len(rune_points)))]
        endShape();
        
def setup():
    size(w, h)
    background(30, 30, 30)
    pixelDensity(2)
    strokeCap(ROUND)
    
    strokeWeight(1)
    
    horizontal_rune_sep = float(grid_pixel_width)/(grid_width - 1)
    vertical_rune_sep = float(grid_pixel_height)/(grid_height - 1)
    
    current_rune = (w/2 - grid_pixel_width/2.0, h/2 - grid_pixel_height/2.0)
    
    for r in range(grid_height):
        for c in range(grid_width):
            opacity_noise = noise(r * noise_scale, c * noise_scale)
            stroke(205, 205, 0, opacity_noise * 255.0)
            strokeWeight(opacity_noise * 3.0)
            
            noFill()
            draw_rune(current_rune[0], current_rune[1], 7, 5, rune_width, rune_height, 2)
            
            current_rune = (current_rune[0] + horizontal_rune_sep, current_rune[1])
        current_rune = (w/2 - grid_pixel_width/2.0, current_rune[1] + vertical_rune_sep)
        
    save("Examples/DifferentColorRunes" + str(int(random(10000))) + ".png")
