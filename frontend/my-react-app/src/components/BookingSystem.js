import React from 'react';
import { useNavigate } from 'react-router-dom';
import './BookingSystem.css';

const BookingSystem = () => {
  const navigate = useNavigate(); // Для перехода между страницами

  return (
    <div>
      <div className="header">
        <h1>Система бронирования ресурсов</h1>
      </div>
      <div className="content container">
        <div className="mb-3">
          {/* Переход на страницу Мониторинга */}
          <button
            className="btn btn-primary"
            onClick={() => navigate('/monitoring')}
          >
            Мониторинг
          </button>
          {/* Переход на страницу Бронирования */}
          <button
            className="btn btn-secondary"
            onClick={() => navigate('/booking')}
          >
            Бронирование
          </button>
          {/* Переход на страницу Настроек */}
          <button
            className="btn btn-dark"
            onClick={() => navigate('/settings')}
          >
            Настройки
          </button>
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
                  <button className="btn btn-warning btn-sm">Перезапустить</button>
                  <button className="btn btn-danger btn-sm">Остановить</button>
                </td>
              </tr>
              <tr>
                <td>Server 2</td>
                <td>Неактивен</td>
                <td>
                  <button className="btn btn-success btn-sm">Запустить</button>
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
