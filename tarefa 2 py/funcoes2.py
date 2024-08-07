def login(perfil):
    if perfil.lower() == 'admin':
        print ('Bem-vindo, Administrador')
    else:
        print ('Bem-vindo, Usuário')
login('Admin')
