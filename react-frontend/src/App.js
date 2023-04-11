import React, { useState, useEffect } from 'react';
import { Helmet } from "react-helmet";
import axios from 'axios';

import './App.css'
  
function App() {
  const [dataForSet, setDataForSet] = useState([]);
  const [dataForGet, setDataForGet] = useState([]);

  const getMetaData = async () => {
    // const base_url = 'https://api-nightly.relmak.com/api/merchant_page_initial_data';
    const base_url = 'http://127.0.0.1:5000/api/merchant_page_initial_data';

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
    setDataForSet(data);
  }

  const showMetadata = async () => {
    // const base_url = 'https://api-nightly.relmak.com/api/merchant_page_initial_data';
    const base_url = 'http://127.0.0.1:5000/api/get_meta_data';

    const siteUrl = 'http://localhost:3000/';

    const res = await axios.get(
      base_url, 
      {
        params: {
          siteUrl: siteUrl,
        },
      });
    const data  = res.data;
    setDataForGet(data);
  }

  return (
    <div className='page-container'>
      <div className="params-container">
        <div className='input-item'>
          {/* <strong>Url</strong>
          <input readOnly value={}/>  */}
          <button type='button' onClick={ getMetaData }>Get Metadata</button>
          <button type='button' onClick={ showMetadata }>Show Metadata</button>
        </div>
        <div className='result-text'>
          <p>{ dataForGet.title }</p>
          <p>{ dataForGet.description }</p>
          <img src={ dataForGet.banner } />
        </div>
      </div>
      <Helmet>
        <title>{ dataForSet.title }</title>
        <meta property="og:title" content={ dataForSet.title }></meta>
        <meta property="og:description" content={ dataForSet.description }></meta>
        <meta property="og:image" content={ dataForSet.banner }></meta>
      </Helmet>
    </div>
  );
}

export default App;
