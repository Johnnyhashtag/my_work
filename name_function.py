def full_formatted_name(f_name, l_name, m_name = ''):
    if m_name:
        full_name = f"{f_name} {m_name} {l_name}"
        
    else:
        full_name = f"{f_name} {l_name}"
    return full_name.title()
