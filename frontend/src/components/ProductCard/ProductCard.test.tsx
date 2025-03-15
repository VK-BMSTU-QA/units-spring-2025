import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);

describe('cards test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard price={999} id = {1} name = {'IPhone 14 Pro'} description = {'Latest iphone, buy it now'} category='Электроника' imgUrl='../../../public/iphone.png'/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add class for selected badge', () => {
        const rendered = render(<ProductCard price={999} id = {1} name = {'IPhone 14 Pro'} description = {'Latest iphone, buy it now'} category='Электроника' imgUrl='../../../public/iphone.png'/>);

        expect(rendered.getByText('IPhone 14 Pro')).toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('Latest iphone, buy it now')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('999 ₽')).toHaveClass(
            'product-card__price'
        );
        expect(rendered.getByText('Электроника')).toHaveClass(
            'product-card__category'
        );
        const imageElement = rendered.getByAltText('IPhone 14 Pro');
        expect(imageElement).toHaveClass('product-card__image');
        
    });

});
