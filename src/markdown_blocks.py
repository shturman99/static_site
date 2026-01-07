def markdwon_to_blocks(text):
    blocks = list(map(lambda x: x.strip(), text.split("\n\n")))
    out = []    
    for block in blocks:
        if block == "":
            continue
        else:
            out.append(block)
    return out