import React, {Component} from 'react';
import {Switch, Route} from 'react-router-dom';
import axios from 'axios';

import Home from './app/Home';
import Header from './app/Header';
import AddLink from './app/AddLink';
import AddCategory from './app/AddCategory';
import LinkDetails from './app/LinkDetails';
import CategoryDetails from './app/CategoryDetails';
import LinkList from './app/LinkList';
import CategoryList from './app/CategoryList';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      receivedData: "",
    }
  }

  componentWillMount() {
    axios({
      method: 'get',
      responseType: 'json',
      url: 'http://127.0.0.1:8000/link-store/',

    })
      .then(response => {
        this.setState({
          receivedData: response.data,
        });
        console.log("data: " + response + "status: " + response.status);
      })
  }


  render() {
    return (
      <div>
        <Header/>
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route path="/add-link" component={AddLink}/>
          <Route path="/add-category" component={AddCategory}/>

          <Route path="/link-details" component={LinkDetails}/>
          <Route path="/category-details" component={CategoryDetails}/>

          <Route path="/link-list" component={LinkList}/>
          <Route path="/categories-list" component={CategoryList}/>
        </Switch>
      </div>
    );
  }
}

export default App;
