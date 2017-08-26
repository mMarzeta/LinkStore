import React, {Component} from 'react';
import axios from 'axios';

export default class AddCategory extends Component {

  handleSubmit(event) {
    this.createCategory(this.refs.title.value, this.refs.description.value);
  }

  createCategory(title, description) {
    axios.post('http://127.0.0.1:8000/link-store/add-category/', {
      title: title,
      description: description
    })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit.bind(this)}>
          <input type="text" ref="title"/>
          <input type="text" ref="description"/>
          <button type="Submit">Add</button>
        </form>
      </div>
    )
  }
}