import React, { Component } from 'react';
import api from '../API'
import '../css/home.css';


 class Home extends React.Component {
  state = {
    loading: true,
    error: null,
    info:null
  };
  async componentDidMount(){
      this.fetchData()
  }
  fetchData = async e => {
      this.setState({loading:true,error:null})
      try{
          const data = await api.actions.listPersons();
          this.setState({info:data});
          console.log(data);
      }catch(error){
        this.setState({loading:false, error:error})
      }
  }
  

  render() {
    return (
      <div className="Home">
        <div className="container">
            <h1>SoftComp</h1>
            
        </div>
      </div>
    );
  }
}
export default Home;