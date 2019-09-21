import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';

import './src/css/global.css';
import App from './src/components/App';


const container = document.getElementById('app');
ReactDOM.render( <App/> , container);