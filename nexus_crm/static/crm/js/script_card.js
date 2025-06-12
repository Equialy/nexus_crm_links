// Функции для редактирования адреса
function editAddress() {
  const displayDiv = document.getElementById("address-display")
  const editDiv = document.getElementById("address-edit")
  const addressText = document.querySelector(".address-text").textContent
  const addressInput = document.getElementById("address-input")

  addressInput.value = addressText
  displayDiv.classList.add("hidden")
  editDiv.classList.remove("hidden")
  addressInput.focus()
}

function saveAddress() {
  const displayDiv = document.getElementById("address-display")
  const editDiv = document.getElementById("address-edit")
  const addressText = document.querySelector(".address-text")
  const addressInput = document.getElementById("address-input")

  addressText.textContent = addressInput.value
  editDiv.classList.add("hidden")
  displayDiv.classList.remove("hidden")

  // Здесь можно добавить AJAX запрос для сохранения на сервере
  console.log("Адрес сохранен:", addressInput.value)

  // Показать уведомление об успешном сохранении
  showNotification("Адрес успешно обновлен", "success")
}

function cancelEdit() {
  const displayDiv = document.getElementById("address-display")
  const editDiv = document.getElementById("address-edit")

  editDiv.classList.add("hidden")
  displayDiv.classList.remove("hidden")
}

// Функция для расчета прибыли
function calculateProfit() {
  const costPrice = Number.parseFloat(document.getElementById("cost-price").value) || 0
  const totalPrice = Number.parseFloat(document.getElementById("total-price").value) || 0
  const profit = totalPrice - costPrice
  const profitInput = document.getElementById("profit")

  profitInput.value = profit.toFixed(2)

  // Изменяем цвет в зависимости от прибыли
  if (profit >= 0) {
    profitInput.style.color = "var(--primary-green)"
  } else {
    profitInput.style.color = "#ef4444"
  }
}

// Функция для обновления расчетов
function updateCosts() {
  const costPrice = document.getElementById("cost-price").value
  const totalPrice = document.getElementById("total-price").value
  const profit = document.getElementById("profit").value

  // Здесь можно добавить AJAX запрос для сохранения на сервере
  console.log("Обновление расчетов:", {
    costPrice: costPrice,
    totalPrice: totalPrice,
    profit: profit,
  })

  // Показать уведомление об успешном обновлении
  showNotification("Расчет стоимости обновлен", "success")
}

// Функция для показа уведомлений
function showNotification(message, type = "info") {
  // Создаем элемент уведомления
  const notification = document.createElement("div")
  notification.className = `notification notification-${type}`
  notification.textContent = message

  // Добавляем стили для уведомления
  notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 20px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    `

  // Устанавливаем цвет в зависимости от типа
  switch (type) {
    case "success":
      notification.style.background = "var(--primary-green)"
      break
    case "error":
      notification.style.background = "#ef4444"
      break
    default:
      notification.style.background = "var(--primary-blue)"
  }

  // Добавляем в DOM
  document.body.appendChild(notification)

  // Анимация появления
  setTimeout(() => {
    notification.style.transform = "translateX(0)"
  }, 100)

  // Удаляем через 3 секунды
  setTimeout(() => {
    notification.style.transform = "translateX(100%)"
    setTimeout(() => {
      document.body.removeChild(notification)
    }, 300)
  }, 3000)
}

// Инициализация при загрузке страницы
document.addEventListener("DOMContentLoaded", () => {
  // Рассчитываем прибыль при загрузке
  calculateProfit()

  // Добавляем обработчики для клавиш
  document.getElementById("address-input").addEventListener("keydown", (e) => {
    if (e.key === "Enter" && e.ctrlKey) {
      saveAddress()
    } else if (e.key === "Escape") {
      cancelEdit()
    }
  })

  // Добавляем анимацию при наведении на карточки
  const cards = document.querySelectorAll(".card")
  cards.forEach((card, index) => {
    card.style.animationDelay = `${index * 0.1}s`
  })

  console.log("Карточка заявки загружена")
})

// Функция для экспорта данных (дополнительная функциональность)
function exportOrderData() {
  const orderData = {
    id: 12345,
    client: {
      name: document.querySelector(".client-name").textContent,
      contacts: Array.from(document.querySelectorAll(".contact-item span")).map((span) => span.textContent),
    },
    address: document.querySelector(".address-text").textContent,
    service: document.querySelector(".service-text").textContent,
    description: document.querySelector(".description").textContent,
    costs: {
      costPrice: document.getElementById("cost-price").value,
      totalPrice: document.getElementById("total-price").value,
      profit: document.getElementById("profit").value,
    },
  }

  console.log("Экспорт данных заявки:", orderData)
  return orderData
}
