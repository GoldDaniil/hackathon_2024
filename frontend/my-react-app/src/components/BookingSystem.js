// src/components/BookingSystem.js
import React from 'react';
import './BookingSystem.css'; // Импортируем CSS-файл для стилей

const BookingSystem = () => {
  const handleButtonClick = (buttonText) => {
    alert(`Вы нажали: ${buttonText}`);
  };

  return (
    <div>
      <div className="header">
        <h1>Система бронирования ресурсов</h1>
      </div>
      <div className="content container">
        <div className="mb-3">
          <button className="btn btn-primary" onClick={() => handleButtonClick('Мониторинг')}>Мониторинг</button>
          <button className="btn btn-secondary" onClick={() => handleButtonClick('Бронирование')}>Бронирование</button>
          <button className="btn btn-dark" onClick={() => handleButtonClick('Настройки')}>Настройки</button>
        </div>
        <div className="server-status">
          <h2>Статус серверов</h2>
          <table className="table table-bordered">
            <thead>
              <tr>
                <th>Сервер</th>
                <th>Статус</th>
                <th>Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Server 1</td>
                <td>Работает</td>
                <td>
                  <button className="btn btn-warning btn-sm" onClick={() => handleButtonClick('Перезапустить')}>Перезапустить</button>
                  <button className="btn btn-danger btn-sm" onClick={() => handleButtonClick('Остановить')}>Остановить</button>
                </td>
              </tr>
              <tr>
                <td>Server 2</td>
                <td>Неактивен</td>
                <td>
                  <button className="btn btn-success btn-sm" onClick={() => handleButtonClick('Запустить')}>Запустить</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default BookingSystem;
