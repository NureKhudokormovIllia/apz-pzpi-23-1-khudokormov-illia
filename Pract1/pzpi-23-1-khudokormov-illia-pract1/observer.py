from abc import ABC, abstractmethod
from typing import List


# ── Інтерфейс спостерігача ─────────────────────────────────────────────────

class Observer(ABC):
    """
    Абстрактний базовий клас (інтерфейс) спостерігача.
    Визначає метод update(), що викликається суб'єктом
    при зміні його стану.
    """

    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        """Отримати сповіщення про зміну стану суб'єкта."""
        pass


# ── Інтерфейс суб'єкта ────────────────────────────────────────────────────

class Subject(ABC):
    """
    Абстрактний базовий клас (інтерфейс) суб'єкта.
    Визначає методи управління списком спостерігачів.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Зареєструвати спостерігача."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Скасувати реєстрацію спостерігача."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Сповістити усіх зареєстрованих спостерігачів."""
        pass


# ── Конкретний суб'єкт ────────────────────────────────────────────────────

class ConcreteSubject(Subject):
    """
    Конкретна реалізація суб'єкта.
    Зберігає стан та список зареєстрованих спостерігачів.
    Автоматично сповіщає спостерігачів при зміні стану.
    """

    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._state: str = ''

    def attach(self, observer: Observer) -> None:
        """Зареєструвати нового спостерігача."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[Subject] Зареєстровано: {observer.__class__.__name__}")

    def detach(self, observer: Observer) -> None:
        """Скасувати реєстрацію спостерігача."""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[Subject] Скасовано реєстрацію: {observer.__class__.__name__}")

    def notify(self) -> None:
        """Сповістити усіх зареєстрованих спостерігачів."""
        print(f"[Subject] Сповіщення {len(self._observers)} спостерігачів...")
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self) -> str:
        """Поточний стан суб'єкта."""
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        """Встановити новий стан та автоматично сповістити спостерігачів."""
        print(f"\n[Subject] Стан змінено: '{self._state}' → '{value}'")
        self._state = value
        self.notify()


# ── Конкретний спостерігач A ──────────────────────────────────────────────

class ConcreteObserverA(Observer):
    """
    Конкретна реалізація спостерігача типу A.
    Синхронізує власний стан зі станом суб'єкта.
    """

    def __init__(self, name: str) -> None:
        self._name = name
        self._observer_state: str = ''

    def update(self, subject: Subject) -> None:
        """Отримати та зберегти новий стан суб'єкта."""
        self._observer_state = subject.state
        print(f"  [{self._name}] Стан оновлено до: '{self._observer_state}'")

    @property
    def observer_state(self) -> str:
        return self._observer_state


# ── Конкретний спостерігач B ──────────────────────────────────────────────

class ConcreteObserverB(Observer):
    """
    Конкретна реалізація спостерігача типу B.
    Реагує на зміни суб'єкта власною логікою.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, subject: Subject) -> None:
        """Відреагувати на зміну стану суб'єкта."""
        state_upper = subject.state.upper()
        print(f"  [{self._name}] Отримано: '{state_upper}' (у верхньому регістрі)")


# ── Демонстрація використання ─────────────────────────────────────────────

def main() -> None:
    print("=" * 60)
    print("Патерн проєктування: Спостерігач (Observer)")
    print("=" * 60)

    # Створення суб'єкта
    subject = ConcreteSubject()

    # Створення спостерігачів
    observer_a = ConcreteObserverA("Спостерігач A")
    observer_b = ConcreteObserverB("Спостерігач B")

    print("\n--- Реєстрація спостерігачів ---")
    subject.attach(observer_a)
    subject.attach(observer_b)

    # Перша зміна стану
    subject.state = "активний"

    # Друга зміна стану
    subject.state = "очікування"

    print("\n--- Скасування реєстрації Спостерігача B ---")
    subject.detach(observer_b)

    # Третя зміна стану (тільки observer_a отримає сповіщення)
    subject.state = "неактивний"

    print("\n--- Перевірка стану Спостерігача A ---")
    print(f"  Поточний стан спостерігача A: '{observer_a.observer_state}'")

    print("\n" + "=" * 60)
    print("Демонстрацію завершено.")


if __name__ == "__main__":
    main()
