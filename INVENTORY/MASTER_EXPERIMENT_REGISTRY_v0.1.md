# CONNECTIONS — MASTER EXPERIMENT REGISTRY v0.1

Generated: 2026-09-26
Status: ACTIVE / CLASSIFICATION PASS 1
Purpose: единый реестр экспериментальных источников Ω-Lab + ORISIK + ARCHIVE без изменения исходников.

## 1. Что реально найдено

Исходный полный inventory содержит 629 файлов-кандидатов:
- OMEGA-LAB: 393
- ORISIK: 234
- ARCHIVE: 2

Важно: 629 ≠ 629 экспериментов. В число входят протоколы, результаты, аудиты, исходный код, тесты, журналы, индексы, исторические записи и дубликаты/копии.

Поиск по ARCHIVE по именам дал только 2 candidate-path, но содержимое самого ARCHIVE показывает, что ARCHIVE является прежде всего provenance/history layer. Поэтому отсутствие слова experiment в имени файла не считается доказательством отсутствия экспериментального материала.

## 2. Нормальная единица учёта

Один эксперимент рассматривается как объект с несколькими артефактами:

EXPERIMENT
├── protocol / preregistration
├── implementation
├── execution evidence
├── raw/derived result
├── audit/control
├── corrected replication
└── historical/provenance links

Файлы внутри одной ветки НЕ считаются независимыми экспериментами автоматически.

## 3. Классы

- EXPERIMENT — постановка/испытание, задающее вопрос и процедуру.
- PROTOCOL — заранее зафиксированный метод/критерии.
- EXECUTION — факт запуска и его provenance.
- RESULT — полученное наблюдение/численный результат.
- AUDIT — проверка корректности постановки или результата.
- CONTROL — отрицательный/положительный/методологический контроль.
- REPLICATION — исправленный или независимый повтор.
- HISTORY — историческая запись.
- SOURCE — исходный материал/код.
- DUPLICATE/VERSION — тот же эксперимент в другой копии/версии.
- NON-EXPERIMENT — индекс, план, архитектура, dossier и т.п.

## 4. Главный принцип

RESULT ≠ TRUTH

RESULT → VERIFY → CLASSIFY → RECORD

Наличие файла, имени EXP-*, PASS или численного вывода само по себе не доказывает научную валидность.

## 5. Уже подтверждённые канонические семейства

### OMEGA-LAB

Подтверждены как отдельные исследовательские семейства/ветки по исходным индексам и содержимому:

- Ω-0
- Ω-MEM-1
- Ω-MEM-2
- Ω-MEM-3
- Ω-MEM-4
- Ω-MEM-4R
- Ω-MEM-5
- Ω-MEM-6
- Ω-MEM-7
- Ω-MEM-8
- Ω-MEM-9
- Ω-INF-1…8
- Ω-B0…B5
- Ω-LINK-1
- Ω-BASIS-002 / R1 / R2
- Ω-EMO-001A / R1
- Ω-PLAN-1
- Ω-FEEDBACK-1
- Ω-FUTURE-1
- Ω-EXECUTION-1
- Ω-VERIFICATION-1
- Ω-CYCLE-1
- Ω-REL-001 и последующие relation-family records
- E-ENERGY series
- E-LIGHT series
- E-MAGNETIC series
- REL-PULSE-01…04
- Ω-TEST-1…12 (с пропусками/результатными файлами, которые требуют отдельного различения)
- Ω-RH-01 research branch
- CICADA-3301 EXP-C1 series
- MARKET EXP-0009…0011
- FOUNDATION / D-R-W-P / MINIMAL-BASIS branch

Это список семейств/идентификаторов, а не утверждение, что каждый файл внутри семьи является отдельным экспериментом.

### ORISIK

Из собственного EXPERIMENT REGISTRY подтверждены как отдельные записи:

- EXP-0001
- EXP-0002
- EXP-0013
- EXP-0014
- EXP-0015
- EXP-0016
- EXP-0017
- EXP-0018
- EXP-AUDIO-001…004
- EXP-VISION-001
- CL-SCALING-001
- CL-SCALING-002
- SPACE baseline
- Ω-ANTI-BH v0.1 / EXPERIMENTS
- Ω-ANTI-BH v0.1 / LAB
- Ω-ANTI-BH v0.2
- MARKET EXP-0001
- MARKET EXP-0002
- RELATIONAL-MEMORY-TEMPORAL-ORDER-001

ORISIK отдельно фиксирует правило: source summary не равен exact copy; EXACT_MATCH требует проверки blob SHA.

## 6. Дедупликация, которую уже можно зафиксировать

### B-Lab / ORISIK EXP-0013…0018

В ORISIK существуют:
- source copies в 04_EXPERIMENTS/RECOVERY/SOURCE/
- research records в 05_RESEARCH/ORGANS/RECOVERY/EXPERIMENTS/

Это две записи одного экспериментального lineage, а не два эксперимента.

### Ω-ANTI-BH v0.1

ORISIK зафиксировал два документа одной experiment family/name/date с разными blob SHA:
- EXPERIMENTS/Ω-ANTI-BH_v0.1.md
- LAB/experiments/omega_anti_bh_v0_1.md

Они классифицируются как RELATED, не EXACT_MATCH.

Ω-ANTI-BH v0.2 — отдельная последующая версия с другим протоколом и статусом DEFER / REWORK.

### CL-SCALING-001

Несколько файлов:
- protocol
- execution
- local result
- parallel result
- partition result

учитываются как один experiment lineage CL-SCALING-001 с несколькими result/execution artifacts.

### Ω-MEM-4 / Ω-MEM-4R

Это НЕ один эксперимент:
- Ω-MEM-4 — исходная постановка с методологическими проблемами.
- Ω-MEM-4R — corrected replication.

Старый результат сохраняется; исправленная репликация не стирает provenance исходной.

### Ω-RH-01

RH-01…RH-64 — не 64 независимых базовых эксперимента автоматически. Это research/attack/audit sequence внутри одной исследовательской ветки Ω-RH-01. Каждый RH-step будет отдельно классифицирован как experiment, attack, computation, audit или result only.

## 7. Evidence status

ORISIK задаёт правильную шкалу:

PLANNED → CODED → EXECUTED → VALIDATED → REPRODUCED

и отдельные:
REJECTED / INVALIDATED

Ключевое правило:
исходник в GitHub не доказывает выполнение.

## 8. Что уже известно о содержательном статусе

ORISIK EXPERIMENT_STATUS_2026-08-20 разделяет:
- PASS — конкретный механизм прошёл конкретный вычислительный тест;
- FAIL — заявленный механизм не прошёл конкретный тест;
- INVALID — постановка не позволяет сделать заявленный причинный вывод.

Зафиксированы, среди прочего, computational PASS для структурной памяти, текущего структурного состояния памяти, жёсткости, связности/притяжения, различия J/C, модельных аттракторов и некоторых constrained-resource механизмов.

Одновременно зафиксированы FAIL/INVALID для ряда более сильных универсальных утверждений, включая часть sink/самозарождения/сверхлинейности/скрытой истории гипотез.

Это не переносится автоматически на физические законы.

## 9. ARCHIVE

ARCHIVE остаётся слоем provenance/history.

Проверенные документы:
- foundation/ANALYSIS_INDEX_v1.0.md
- imports/SPACE-2026-08-15/test-evidence.md

ARCHIVE прямо говорит:
- map ≠ evidence;
- при важном утверждении нужно идти к original source;
- цепочка continuity: ARCHIVE → CORE → SPACE → LAB evidence → implementation → CI/test → status → next work.

Следовательно, архивные материалы должны быть связаны с экспериментами как provenance/history, а не автоматически превращаться в новые эксперименты.

## 10. Следующий проход

PASS 2 должен сделать для каждого канонического ID:

ID | question | protocol | implementation | execution evidence | result | audit/control | replication | status | source SHA | related IDs | CONNECTIONS relevance

Особенно нужно пройти:
1. Ω-REL family;
2. E-ENERGY family;
3. Ω-MEM family;
4. Ω-INF family;
5. Ω-LINK / BASIS / EMO;
6. Ω-TEST-1…12;
7. Ω-RH-01;
8. CICADA;
9. ORISIK relational-memory / boundary / attractor / black-hole branches;
10. B-Lab EXP-0001…0018;
11. MARKET experiments;
12. все source/result пары и exact-copy relations.

## 11. Запреты

- Не переносить 629 файлов как 629 экспериментов.
- Не заменять source result пересказом.
- Не удалять старые результаты после corrected replication.
- Не объединять разные SHA только по похожему имени.
- Не считать CI PASS доказательством более широкого утверждения.
- Не считать planned/coded материал executed.
- Не повышать semantic similarity до EXACT_MATCH.

## 12. Source of truth

Полный сырой inventory:
INVENTORY/EXPERIMENT_SOURCE_INVENTORY_2026-09-26.md

Канонический ORISIK registry:
04_EXPERIMENTS/EXPERIMENT_REGISTRY.md

Центральная evidence policy:
05_RESEARCH/ORGANISM/EVIDENCE_INDEX.md
05_RESEARCH/ORGANISM/EXPERIMENT_STATUS_2026-08-20.md
05_RESEARCH/ORGANISM/MASTER_CLASSIFICATION_MATRIX_v0.1.md

Этот файл — рабочий master registry CONNECTIONS, не замена исходным документам.
