Característica: Inicio de sesión en SauceDemo.com

  Como usuario de SauceDemo
  Quiero iniciar sesión
  Para acceder al inventario de productos

  @smoke
  Escenario: Inicio de sesión exitoso
    Dado que el usuario está en la página de login
    Cuando ingresa el usuario "standard_user" y la contraseña "secret_sauce"
    Entonces debe acceder al inventario

  Escenario: Inicio de sesión con usuario bloqueado
    Dado que el usuario está en la página de login
    Cuando ingresa el usuario "locked_out_user" y la contraseña "secret_sauce"
    Entonces debe visualizar un mensaje de usuario bloqueado