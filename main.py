
from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion
from clinica import Clinica


# Crear una instancia de la clínica
clinica = Clinica()


# ==========================================
# 1. REGISTRO DE PACIENTE
# ==========================================

paciente_01 = Paciente("P001", "Juan", 22)
clinica.agregar_paciente(paciente_01)


# ==========================================
# 2. REGISTRO DE MÉDICO
# ==========================================

medico_01 = Medico("M001", "Oscar Torres", "Cardiologia")
clinica.agregar_medico(medico_01)


# ==========================================
# 3. REGISTRO DE CITA
# ==========================================

cita_01 = Cita("C001", paciente_01, medico_01, "04/11/2026")
clinica.agregar_cita(cita_01)


# ==========================================
# 4. MOSTRAR INFORMACIÓN REGISTRADA
# ==========================================

print("\n========== SISTEMA KAWSAY ==========")

print("\n--- PACIENTES REGISTRADOS ---")
paciente_01.resumen()

print("\n--- MÉDICOS REGISTRADOS ---")
medico_01.resumen()

print("\n--- CITAS REGISTRADAS ---")
cita_01.resumen()


# ==========================================
# 5. BÚSQUEDA POR CÓDIGO
# ==========================================

print("\n--- BÚSQUEDA DE PACIENTE ---")

resultado = clinica.buscar_por_codigo("P001")

if resultado:
    resultado.resumen()
else:
    print("No se encontró el registro.")


print("\n--- BÚSQUEDA DE CÓDIGO INEXISTENTE ---")

resultado = clinica.buscar_por_codigo("P999")

if resultado:
    resultado.resumen()
else:
    print("No se encontró el registro.")


# ==========================================
# 6. REGISTRO DE ATENCIÓN MÉDICA
# ==========================================

atencion_01 = Atencion(
    "A001",
    cita_01,
    "Hipertension leve",
    "Dieta baja en sal"
)

print("\n--- REGISTRO DE ATENCIÓN ---")
clinica.registrar_atencion(atencion_01)


# ==========================================
# 7. MOSTRAR HISTORIAL MÉDICO
# ==========================================

print("\n--- HISTORIAL MÉDICO ---")
clinica.mostrar_historial()


# ==========================================
# 8. FILTRAR CITAS POR PACIENTE
# PROGRAMACIÓN FUNCIONAL: FILTER Y LAMBDA
# ==========================================

print("\n--- CITAS DEL PACIENTE P001 ---")

citas_filtradas = clinica.filtrar_citas_por_paciente("P001")

if citas_filtradas:
    for cita in citas_filtradas:
        cita.resumen()
else:
    print("No se encontraron citas para este paciente.")


# ==========================================
# 9. FILTRAR ATENCIONES POR PACIENTE
# PROGRAMACIÓN FUNCIONAL: FILTER Y LAMBDA
# ==========================================

print("\n--- ATENCIONES DEL PACIENTE P001 ---")

atenciones_filtradas = clinica.filtrar_atenciones_por_paciente("P001")

if atenciones_filtradas:
    for atencion in atenciones_filtradas:
        atencion.resumen()
else:
    print("No se encontraron atenciones para este paciente.")


print("\n========== FIN DEL SISTEMA KAWSAY ==========")
