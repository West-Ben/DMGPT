import React, { useState, useEffect } from 'react';
import ItemList from './components/ItemList';
import { fetchItems } from './utils/api';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    async function getItems() {
      const items = await fetchItems();
      setItems(items);
    }
    getItems();
  }, []);

  return (
    <div className="App">
      <h1>My FastAPI React App</h1>
      <ItemList items={items} />
    </div>
  );
}

export default App;