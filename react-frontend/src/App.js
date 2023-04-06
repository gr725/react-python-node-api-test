import React, { useState, useEffect } from 'react';
import axios from 'axios';

import './App.css'

function App() {
  const [result, setResult] = useState([]);


  const callApi = async () => {
    const base_url = 'https://api-nightly.relmak.com/api/merchant_page_initial_data';

    const path = 'John';
    const titleQuery = 'title';
    const descQuery = 'desc';

    const res = await axios.get(
      `${base_url}/${path}`, 
      {
        params: {
          title: titleQuery,
          description: descQuery,
        },
      });
    const data  = res.data;
    console.log(data);
  }

  return (
    <div className='page-container'>
      <div className="params-container">

      <button type='button' onClick={ callApi }>Call</button>
      <span className='result-text'>{ result }</span>
    </div>
    </div>
  );
}

export default App;
