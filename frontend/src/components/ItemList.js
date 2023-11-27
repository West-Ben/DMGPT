// frontend/src/components/ItemList.js

import React, { useState, useEffect } from 'react';
import { fetchItems } from '../utils/api';

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    async function getItems() {
      const items = await fetchItems();
      setItems(items);
    }
    getItems();
  }, []);

  return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ItemList;