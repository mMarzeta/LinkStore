import React, {Component} from 'react';
import {Link} from 'react-router-dom';

export default class Header extends Component {
  render() {
    return (
      <div>
        <ul>
          <li><Link to="/">Link Store</Link></li>
          <li><Link to="/add-link">Add link</Link></li>
          <li><Link to="/add-category">Add Category</Link></li>
          <li><Link to="/link-list">Links</Link></li>
          <li><Link to="/categories-list">Categories</Link></li>
        </ul>
      </div>
    )
  }
}