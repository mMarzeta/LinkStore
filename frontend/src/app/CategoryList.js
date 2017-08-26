import React, {Component} from 'react';
import axios from 'axios';

export default class CategoryList extends Component {
  constructor(props){
    super(props);

    this.state = {
      categories: []
    }
  }

  componentDidMount(){
    axios.get('http://127.0.0.1:8000/link-store/categories-list/')
      .then(response => {
        const categories = response.data.map(obj => JSON.parse(obj));
        this.setState({ categories });
        console.log(response.data);
        console.log(this.state.categories);
      })
  }

  render() {
    return (
      <div>
        <h1>Categories:</h1>
        <ul>
          {this.state.categories.map(category =>
            <li key={category.pk}>{category.pk}) {category.title} : {category.description}</li>
          )}
        </ul>
      </div>
    )
  }
}