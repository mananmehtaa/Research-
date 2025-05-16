import React, { useEffect, useState } from 'react';

function App() {
  const [imuData, setImuData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      fetch('http://localhost:8000/data')
        .then(res => res.json())
        .then(data => setImuData(data))
        .catch(err => console.error("Fetch error:", err));
    };

    fetchData();
    const interval = setInterval(fetchData, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: '2rem', backgroundColor: '#0a0a0a', color: '#ffffff' }}>
      <h1>LiDAR IMU Data Viewer</h1>
      <table border="1" cellPadding="8" style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>ID</th>
            <th>Qx</th>
            <th>Qy</th>
            <th>Qz</th>
            <th>Qw</th>
            <th>Delay (µs)</th>
          </tr>
        </thead>
        <tbody>
          {imuData.map((row, idx) => (
            <tr key={idx}>
              {row.map((value, i) => (
                <td key={i}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
