def rgb(r, g, b): 
    hexa_code = ""
    hexa_num = "0123456789ABCDEF"
    for x in [r,g,b]:
        if x < 0: hexa_code += "00"
        elif x > 255: hexa_code += "FF"      
        else: hexa_code += hexa_num[x//16] + hexa_num[(x%16)]

    return hexa_code

def hex_tra(hex_rgb):
    hexa_num = "0123456789ABCDEF"
    rgb = []
    num_value = 0
    for i in range(6): 
        if i % 2: 
            num_value += hexa_num.find(hex_rgb[i])+1
        else: 
            num_value = (hexa_num.find(hex_rgb[i]))*16  
            rgb.append(num_value)

    return rgb  