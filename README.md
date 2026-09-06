# data-science-small-researches

Реализации классических алгоритмов машинного обучения с нуля на NumPy и два прикладных проекта на открытых данных. Учебный репозиторий: цель — не собрать модель из готовых компонентов, а написать её изнутри и понять, из чего она состоит.

![Python](https://img.shields.io/badge/python-3.9-blue)
![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange)

## Содержание

- [Что внутри](#что-внутри)
- [Алгоритмы с нуля](#алгоритмы-с-нуля)
- [Прикладные проекты](#прикладные-проекты)
- [Запуск](#запуск)
- [Стек](#стек)
- [Источники и лицензия](#источники-и-лицензия)

## Что внутри

| Каталог | Содержание |
|---|---|
| [`Yandex_ML4.0/`](Yandex_ML4.0) | Девять заданий курса Yandex ML Training: базовые алгоритмы, реализованные на NumPy без готовых решений |
| [`projects/`](projects) | Два самостоятельных проекта полного цикла — от разведочного анализа до интерпретации модели |

## Алгоритмы с нуля

В каждом задании ноутбук с исследованием и отдельный модуль с реализацией. Модуль — это и есть результат: код в нём написан вручную, sklearn используется только как эталон для сверки.

| Задание | Что реализовано | Модуль |
|---|---|---|
| 01 · k ближайших соседей | Класс `KNearestNeighbor`: обучение, предсказание и три способа посчитать матрицу расстояний — на двух циклах, на одном и полностью векторизованно | [`k_nearest_neighbor.py`](Yandex_ML4.0/assignment01_knn/k_nearest_neighbor.py) |
| 02 · Распределение Лапласа | Класс `LaplaceDistribution`: оценка параметров через медиану и среднее абсолютное отклонение, `pdf` и `logpdf` | [`distribution.py`](Yandex_ML4.0/assignment02_laplace/distribution.py) |
| 03 · Функции потерь и производные | `LossAndDerivatives`: MSE, MAE, L1- и L2-регуляризация и аналитические производные каждой из них | [`derivatives.py`](Yandex_ML4.0/assignment03_derivatives/derivatives.py) |
| 04 · Степенной метод | Поиск наибольшего собственного значения и соответствующего собственного вектора итерациями | [`power_iteration.py`](Yandex_ML4.0/assignment04_power_iteration/power_iteration.py) |
| 05 · Бэггинг и OOB | `SimplifiedBaggingRegressor`: бутстрэп-выборки, усреднение предсказаний и out-of-bag оценка качества без отложенной выборки | [`bagging.py`](Yandex_ML4.0/assignment05_bagging_and_oob/bagging.py) |
| 06 · Градиентный бустинг | `SimplifiedBoostingRegressor`: последовательное обучение деревьев на антиградиенте функции потерь | [`boosting.py`](Yandex_ML4.0/assignment06_boosting/boosting.py) |
| 07 · Классификация MNIST | Классификация рукописных цифр | ноутбук |
| 08 · Важность признаков | Оценка важности признаков на данных о продажах автомобилей | ноутбук |
| 09 · Итоговое задание | Финальная работа курса | ноутбук |

## Прикладные проекты

### Project 1 — «Титаник»: точка входа в анализ данных

Бинарная классификация: выжил ли пассажир. Задача учебная и намеренно простая — интерес в том, чтобы пройти полный цикл целиком, а не в метрике.

Что отработано: загрузка данных с Kaggle, первичный осмотр и заполнение пропусков, графики для поиска зависимостей, подготовка признаков, модели sklearn, кросс-валидация и матрица ошибок, подбор гиперпараметров, интерпретация модели через SHAP.

Данные: [Titanic — Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data).

### Project 2 — отчисление или успех студента

Мультиклассовая классификация: студент бросит учёбу, успешно завершит её или останется на том же курсе.

Что отработано: сводные таблицы, снижение размерности через PCA, отбор значимых признаков, выбор моделей под характер данных, несколько способов смешивания моделей.

Данные: [Predict students' dropout and academic success](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention).

## Запуск

```bash
git clone https://github.com/HasagiGr/data-science-small-researches.git
cd data-science-small-researches

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook
```

Ноутбуки заданий также открываются в Colab — ссылка есть в `README.md` внутри каждого каталога задания.

## Стек

Python 3.9, NumPy, pandas, scikit-learn, Matplotlib, SHAP, Jupyter.

## Источники

Задания в `Yandex_ML4.0/` — шаблоны курса [girafe-ai/ml-course](https://github.com/girafe-ai/ml-course) (поток Yandex ML Training). Формулировки задач и заготовки принадлежат авторам курса; в этом репозитории лежат мои решения.
