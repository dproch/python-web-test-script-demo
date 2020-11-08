from selene import have
from selene.support.shared import browser

# Arrange
browser.open('http://todomvc.com/examples/emberjs/')

# Act
browser.element('[id="new-todo"]').type('listen lesson').press_enter()
browser.element('[id="new-todo"]').type('have a rest').press_enter()
browser.element('[id="new-todo"]').type('do homework').press_enter()

# Assert
browser.all('[id="todo-list"] li').should(have.exact_texts('listen lesson', 'have a rest', 'do homework'))
