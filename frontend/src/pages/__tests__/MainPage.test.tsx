import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import { getProducts } from '../../mocks/productMocks';
import '@testing-library/jest-dom';
import { Product } from '../../types';
import { useProducts } from '../../hooks';

const CURRENT_TIME: string = '20:31:00';
jest.mock('../../hooks', () => ({
  useCurrentTime: jest.fn(() => CURRENT_TIME),
  useProducts: jest.fn(() => getProducts()),
}));

afterEach(jest.clearAllMocks);

describe('Testing MainPage', () => {
  it('rendered main page', () => {
    const mainPage = render(<MainPage />);
    expect(mainPage.asFragment()).toMatchSnapshot();
  });

  it('returning current time', () => {
    const mainPage = render(<MainPage />);
    expect(mainPage.getByText(CURRENT_TIME)).toBeInTheDocument();
  })

  it('return all products if no category selected', () => {
    const mainPage = render(<MainPage />);
    const products: Product[] = useProducts();
    products.forEach((product) => {
      expect(mainPage.getByText(product.name)).toBeInTheDocument();
    });
  });

  it('return filtered products if one category selected', () => {
    const mainPage = render(<MainPage />);
    const products: Product[] = useProducts();
    const electronicsCategories = mainPage.getAllByText('Электроника');
    const electronicsBadge = electronicsCategories.find(el => el.classList.contains('categories__badge'));
    if (!electronicsBadge) {
      throw new Error('Cant find category: "Электроника"');
    }

    fireEvent.click(electronicsBadge);
    products.forEach((product) => {
      if (product.category === 'Электроника') {
        expect(mainPage.getByText(product.name)).toBeInTheDocument();
      } else {
        expect(mainPage.queryByText(product.name)).not.toBeInTheDocument();
      }
    });
  });
  
  it('return filtered products if multiple categories selected', () => {
    const mainPage = render(<MainPage />);
    const products: Product[] = useProducts();
   
    const categories: string[] = ['Электроника', 'Одежда']
    categories.forEach((category) => {
      const foundCategories = mainPage.getAllByText(category);
      const badge = foundCategories.find(el => el.classList.contains('categories__badge'));
      if (!badge) {
        throw new Error(`Cant find category: ${category}`);
      }
      fireEvent.click(badge);
    });

    products.forEach((product) => {
      if (categories.includes(product.category)) {
        expect(mainPage.getByText(product.name)).toBeInTheDocument();
      } else {
        expect(mainPage.queryByText(product.name)).not.toBeInTheDocument();
      }
    });
  });

  it('return filtered products if categories unselected', () => {
    const mainPage = render(<MainPage />);
    const products: Product[] = useProducts();
    const electronicsCategories = mainPage.getAllByText('Электроника');
    const electronicsBadge = electronicsCategories.find(el => el.classList.contains('categories__badge'));
    if (!electronicsBadge) {
      throw new Error('Cant find category: "Электроника"');
    }
  
    fireEvent.click(electronicsBadge);
    fireEvent.click(electronicsBadge);
    
    products.forEach((product) => {
      expect(mainPage.getByText(product.name)).toBeInTheDocument();
    });
  });
});