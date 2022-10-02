from view import render_template
from database.models import Student, Teacher
from add_users import create_teacher, create_student


def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default.jinja2", cls=cls)
    s = input(">> ")
    return s, None


def show_all_teacher(data=None, cls=True):
    """Все записи"""
    teachers = Teacher.all()
    render_template(context={'teachers': teachers}, template="show_all.jinja2", cls=cls)
    state = input("Продолжить?\n(yes/no)\n>> ").lower()
    if state == 'no' or state == 'n':
        exit_controller(data=None, cls=True)
    elif state == 'yes' or state == 'y':
        return 'main', None
    else:
        raise ValueError(f"Неизвестно значение {state}")


def exit_controller(data=None, cls=True):
    """Выход"""
    render_template(context={'count': 1}, template="exit.jinja2", cls=cls)
    exit()


def add_teacher(data=None, cls=True):
    """Добавить учителя"""
    context = create_teacher(cls)
    render_template(context=context, template="add_teacher.jinja2", cls=cls)
    state = input('>> ')
    if state == '1':  # - Добавить студента
        teacher = Teacher.add(name=context['name'], surname=context['surname'])
        return 777, teacher
    elif state == '2':
        Teacher.add(name=context['name'], surname=context['surname'])
        return exit_controller()
    elif state == '3':
        exit_controller(cls)
    else:
        raise ValueError(f'Неверное значение {state}')


def add_student(teacher, cls=True):
    """Добавление студента"""
    while True:
        student = create_student(cls)
        render_template(context=student, template="add_student.jinja2", cls=cls)
        step = input(">")
        if step == '1':
            Student.add(name=student['name'], surname=student['surname'], age=student['age'], phone=student['phone'],
                        teacher=teacher)
            continue

        elif step == '2':
            return 'main', None

        else:
            raise ValueError(f"Неизвестное значение {step}")


def get_controller(state):
    """Контроллер"""
    return CONTROLLERS_DICT.get(state, default_controller)


CONTROLLERS_DICT = {
    '0': exit_controller,
    '1': show_all_teacher,
    '2': add_teacher,
    777: add_student

}
