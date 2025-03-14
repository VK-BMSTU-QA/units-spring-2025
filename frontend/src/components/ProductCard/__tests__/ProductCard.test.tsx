import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from '../ProductCard';
import { getPrice } from '../../../utils';

jest.mock('../../../utils', () => ({
    getPrice: jest.fn((price, symbol) => `${symbol}${price}`),
}));

afterEach(jest.clearAllMocks);

describe('test ProductCard component', () => {
    it('should render correctly and match snapshot', () => {
        const rendered = render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
                imgUrl="/mock-image.jpg"
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render the product name', () => {
        render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
                imgUrl="/mock-image.jpg"
            />
        );

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('should render the product description', () => {
        render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
                imgUrl="/mock-image.jpg"
            />
        );

        expect(
            screen.getByText('Latest iphone, buy it now')
        ).toBeInTheDocument();
    });

    it('should render the product price with symbol', () => {
        render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
                imgUrl="/mock-image.jpg"
            />
        );

        expect(screen.getByText('$999')).toBeInTheDocument();
        expect(getPrice).toHaveBeenCalledWith(999, '$');
    });

    it('should render the product category', () => {
        render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
                imgUrl="/mock-image.jpg"
            />
        );

        expect(screen.getByText('Электроника')).toBeInTheDocument();
    });

    it('should render an image if imgUrl is provided', () => {
        render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
                imgUrl="/mock-image.jpg"
            />
        );

        const image = screen.getByAltText('IPhone 14 Pro');
        expect(image).toBeInTheDocument();
        expect(image).toHaveAttribute('src', '/mock-image.jpg');
    });

    it('should not render an image if imgUrl is not provided', () => {
        render(
            <ProductCard
                name="IPhone 14 Pro"
                description="Latest iphone, buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={1}
            />
        );

        const image = screen.queryByAltText('IPhone 14 Pro');
        expect(image).not.toBeInTheDocument();
    });
});
