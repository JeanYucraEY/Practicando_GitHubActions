# 📊 Guía Visual de Workflows

Esta guía muestra gráficamente cómo funcionan los workflows disponibles.

## Evento: PUSH a Main o Develop

```
┌─────────────────────────────────────────────────────────────────┐
│ Git Push a rama main/develop o manual workflow_dispatch         │
└────────────┬────────────────────────────────────────────────────┘
             │
             v
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 01-hello-world.yml COMIENZA                                  │
│                                                                  │
│  Step 1: Checkout código                                        │
│  Step 2: Say Hello                                              │
│  Step 3: Show System Info                                       │
│  Step 4: Check if is PR (if applicable)                         │
│                                                                  │
│ ✅ COMPLETADO en ~30 segundos                                   │
└──────────────────────────────────────────────────────────────────┘
             │
             v
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 02-python-tests.yml COMIENZA (en paralelo)                   │
│                                                                  │
│  Matrix: Python 3.9, 3.10, 3.11                                 │
│  ├─ Instala Python X.Y                                          │
│  ├─ Instala dependencias (pip)                                  │
│  ├─ Ejecuta tests con pytest                                    │
│  └─ Genera coverage report                                      │
│                                                                  │
│ ✅ COMPLETADO en ~2 minutos (3 versiones en paralelo)          │
└──────────────────────────────────────────────────────────────────┘
             │
             v
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 03-multi-job.yml COMIENZA (en serie)                         │
│                                                                  │
│  [BUILD]       ✅ Crea artefacto                                │
│     │                                                            │
│     v                                                            │
│  [TEST]        ✅ Descarga artefacto, ejecuta tests             │
│     │                                                            │
│     v                                                            │
│  [DEPLOY]      ✅ Solo si rama es main                          │
│     │                                                            │
│     v                                                            │
│  [NOTIFY]      ✅ Siempre, reporta status                       │
│                                                                  │
│ ✅ COMPLETADO en ~3 minutos                                     │
└──────────────────────────────────────────────────────────────────┘
```

---

## Evento: PULL REQUEST contra Main

```
┌─────────────────────────────────────────────────────────────────┐
│ Pull Request ABIERTO/ACTUALIZADO                                │
└────────────┬────────────────────────────────────────────────────┘
             │
             v
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 05-on-pull-request.yml COMIENZA                              │
│                                                                  │
│  Step 1: Get PR Information                                     │
│  Step 2: Check file changes (git diff)                          │
│  Step 3: Lint changes (busca TODO/FIXME)                        │
│  Step 4: Add PR comment automático                              │
│                                                                  │
│ 💬 Resultado: Comentario en el PR                               │
│ ✅ COMPLETADO en ~1 minuto                                      │
└──────────────────────────────────────────────────────────────────┘
```

---

## Evento: SCHEDULED (Cron)

```
┌─────────────────────────────────────────────────────────────────┐
│ CADA DÍA a las 10:00 UTC (o manual workflow_dispatch)           │
└────────────┬────────────────────────────────────────────────────┘
             │
             v
   ┌─────────────────────────┐
   │ 10:00 UTC Diariamente   │
   │ Ejecuta automáticamente │
   └─────────────┬───────────┘
                 │
                 v
┌──────────────────────────────────────────────────────────────────┐
│ ✅ 04-scheduled.yml COMIENZA                                    │
│                                                                  │
│  Step 1: Run scheduled task (date/time)                         │
│  Step 2: Check repository status                                │
│  Step 3: Run maintenance tasks                                  │
│                                                                  │
│ 📊 Ideal para: Limpiar, generar reportes, backups              │
│ ✅ COMPLETADO en ~1 minuto                                      │
└──────────────────────────────────────────────────────────────────┘
```

---

## Evento: WORKFLOW DISPATCH (Manual)

```
┌────────────────────────────────────────────────────────────────┐
│ Usuario hace clic en Actions → Run Workflow                    │
│ Completa el formulario de inputs                               │
└────────────┬──────────────────────────────────────────────────┘
             │
             v
┌────────────────────────────────────────────────────────────────┐
│ ✅ 06-with-environment-variables.yml COMIENZA                 │
│                                                                │
│  Input 1: environment = 'production'                           │
│  Input 2: log_level = 'debug'                                  │
│                                                                │
│  Step 1: Show all variables                                    │
│          ├─ GLOBAL_VAR                                         │
│          ├─ JOB_ENV                                            │
│          ├─ ENVIRONMENT (del input)                            │
│          └─ LOG_LEVEL (del input)                              │
│                                                                │
│  Step 2: Step with local variables                             │
│          ├─ STEP_VAR                                           │
│          ├─ BRANCH (github.ref_name)                           │
│          ├─ WORKFLOW (github.workflow)                         │
│          └─ RUN_ID (github.run_id)                             │
│                                                                │
│  Step 3: Use secrets                                           │
│          └─ API_KEY (del secrets)                              │
│                                                                │
│ ✅ COMPLETADO en ~30 segundos                                  │
└────────────────────────────────────────────────────────────────┘
```

---

## Matriz de Ejecución (02-python-tests.yml)

```
┌──────────────────────────────────────────────────────────────────┐
│ MATRIX: Python [3.9, 3.10, 3.11]                                │
└──────────────────────────────────────────────────────────────────┘

 Timestamp    Python     Steps
 ──────────   ────────   ────────────────────────────
 10:00:00     3.9        ✅ Setup → Install → Test → Coverage
              ↓
 10:00:30     3.10       ✅ Setup → Install → Test → Coverage
 (paralelo)   ↓
 10:01:00     3.11       ✅ Setup → Install → Test → Coverage

 ✅ Todos terminan ~aprox. 10:02:00 (el más lento)
```

---

## Flujo de Dependencias (03-multi-job.yml)

```
NECESIDAD DE EJECUCIÓN:

┌────────┐
│ BUILD  │  ← Primero                    ~30s
└────┬───┘
     │
     v
┌────────┐
│ TEST   │  ← Después de BUILD           ~1m
└────┬───┘
     │
     v
┌────────┐
│DEPLOY  │  ← Después de TEST            ~1m
│        │  ← Solo si rama == main
└────┬───┘
     │
     v
┌────────┐
│ NOTIFY │  ← Siempre al final           ~10s
│        │  ← even si BUILD o TEST fallan
└────────┘

TIEMPO TOTAL: ~2:40 segundos (secuencial)
```

---

## Status de Workflows

```
Durante Ejecución:
┌─────────────────────┬──────────────────┐
│ 01-hello-world      │ ⏳ In progress    │
├─────────────────────┼──────────────────┤
│ 02-python-tests     │ ⏳ In progress    │
├─────────────────────┼──────────────────┤
│ 03-multi-job        │ ⏳ In progress    │
└─────────────────────┴──────────────────┘

Después de completar:
┌─────────────────────┬──────────────────┐
│ 01-hello-world      │ ✅ Completed     │
├─────────────────────┼──────────────────┤
│ 02-python-tests     │ ✅ Completed     │
├─────────────────────┼──────────────────┤
│ 03-multi-job        │ ❌ Failed        │
└─────────────────────┴──────────────────┘

Con Eventos:
┌─────────────────────┬──────────────────┐
│ 04-scheduled        │ ⏰ Scheduled      │
├─────────────────────┼──────────────────┤
│ 05-on-pull-request  │ 🔔 Waiting PR    │
├─────────────────────┼──────────────────┤
│ 06-env-variables    │ ⏸️  Ready manual  │
└─────────────────────┴──────────────────┘
```

---

## Matriz de Triggers

```
Workflow                    | Push | PR   | Schedule | Manual
─────────────────────────────────────────────────────────────────
01-hello-world              | ✅   | ✅   | ❌       | ✅
02-python-tests             | ✅   | ✅   | ❌       | ❌
03-multi-job                | ✅   | ❌   | ❌       | ❌
04-scheduled                | ❌   | ❌   | ✅       | ✅
05-on-pull-request          | ❌   | ✅   | ❌       | ❌
06-with-env-variables       | ✅   | ❌   | ❌       | ✅
```

---

## Arquitectura de Artefactos

```
03-multi-job.yml:

JOB: BUILD
├─ Step: Compile code
└─ Output: build/app.txt
   │
   └─→ ARTIFACT: build-artifact
       │
       └─→ Almacenado en GitHub

        ↓ (descarga)

JOB: TEST
├─ Download: build-artifact
├─ Step: Execute tests
└─ Status: ✅ Pass / ❌ Fail

        ↓ (descarga)

JOB: DEPLOY
├─ Download: build-artifact
├─ Step: Deploy to prod
└─ Status: ✅ Complete
```

---

**¡Visualiza tus workflows con estos diagramas!** 📊
