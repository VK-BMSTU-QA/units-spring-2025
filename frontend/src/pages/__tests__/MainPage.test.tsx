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

  it('return filtered products if categories selected', () => {
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
      }
    });
  });
});