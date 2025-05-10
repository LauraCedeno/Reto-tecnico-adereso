Feature: Gestión de Intenciones

  Background: El usuario está en la sección de intenciones
    When el usuario navega a la sección de intenciones

  Scenario: Inicio de sesión exitoso
    Then debería ver la página principal # Puedes tener una verificación adicional aquí si lo deseas

  Scenario: Crear una nueva intención
    When hace clic en el botón para crear una nueva intención
    And completa el formulario con nombre "REPROGRAMAR_CITA", descripción "El usuario quiere reprogramar su cita" y ejemplo "Ejemplo de prueba"
    And hace clic en el botón de guardar
    Then debería ver la intención "Intención de prueba" en la lista


