import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard id={10} name='Strange'
            description='Strangest'
            price={100}
            priceSymbol='$'
            category='Для дома'
            imgUrl="test.jpg" />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
    
});
