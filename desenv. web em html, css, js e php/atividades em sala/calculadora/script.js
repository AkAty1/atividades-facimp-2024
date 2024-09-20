const screen = document.getElementById('screen');
const buttons = document.querySelectorAll('.btn');
const clearButton = document.getElementById('clear');
const equalButton = document.getElementById('equal');
const backspaceButton = document.getElementById('backspace');

let currentInput = '';
let operator = '';
let previousInput = '';

buttons.forEach(button => {
    button.addEventListener('click', () => {
        if (button.classList.contains('operator')) {
            operator = button.value;
            previousInput = currentInput;
            currentInput = '';
        } else if (button.value === '%') {
            calculatePercentage();
        } else {
            currentInput += button.value;
        }
        screen.value = currentInput;
    });
});

equalButton.addEventListener('click', () => {
    if (previousInput && currentInput && operator) {
        let result;
        const prev = parseFloat(previousInput);
        const current = parseFloat(currentInput);
        switch (operator) {
            case '+':
                result = prev + current;
                break;
            case '-':
                result = prev - current;
                break;
            case '*':
                result = prev * current;
                break;
            case '/':
                result = prev / current;
                break;
        }
        screen.value = result;
        currentInput = result.toString();
        previousInput = '';
        operator = '';
    }
});

clearButton.addEventListener('click', () => {
    currentInput = '';
    previousInput = '';
    operator = '';
    screen.value = '';
});

backspaceButton.addEventListener('click', () => {
    currentInput = currentInput.slice(0, -1);
    screen.value = currentInput;
});

function calculatePercentage() {
    if (currentInput) {
        const percentageValue = parseFloat(currentInput) / 100;
        screen.value = percentageValue;
        currentInput = percentageValue.toString(); 
    }
}
