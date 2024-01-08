boat = 'left'
m_left = 3
c_left =3
m_right = 0
c_right = 0

print(c_left * '\U0001f482',m_left * '\U0001f479','|','\U0001f6A2', 4*'\U0001f30a','|',c_right * '\U0001f482', m_right *'\U0001f479' )
while('True'):
    m= int(input())
    n = int(input())
    s = m+n
    if( (s != 2) and s !=1):
        print("invalid move")
    if(boat == 'left'):
        m_left -= m
        c_left -= n
        m_right += m
        c_right += n
        print(c_left * '\U0001f482',m_left * '\U0001f479','|', 4*'\U0001f30a', '\U0001f6A2','|',c_right * '\U0001f482', m_right *'\U0001f479' )
        boat = 'right'
    else:
        m_left += m
        c_left += n
        m_right -= m
        c_right -= n
        print(c_left * '\U0001f482',m_left * '\U0001f479','|','\U0001f6A2', 4*'\U0001f30a','|',c_right * '\U0001f482', m_right *'\U0001f479' )
        boat = 'left'
    if((c_right<m_right and c_right> 0) or (c_left<m_left and c_left > 0)):
        print("invlaid game")
        break
    if(c_right == 3 and m_right == 3):
        print("you won")
        break