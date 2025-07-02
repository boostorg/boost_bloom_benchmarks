# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.54</td>
    <td align="right">6.14</td>
    <td align="right">4.27</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.07</td>
    <td align="right">12.08</td>
    <td align="right">18.09</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.41</td>
    <td align="right">5.06</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.62</td>
    <td align="right">18.01</td>
    <td align="right">19.25</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.40</td>
    <td align="right">5.17</td>
    <td align="right">5.18</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.35</td>
    <td align="right">21.57</td>
    <td align="right">18.15</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.03</td>
    <td align="right">5.64</td>
    <td align="right">5.65</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">6.03</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.39</td>
    <td align="right">27.73</td>
    <td align="right">18.54</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.83</td>
    <td align="right">6.31</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.02</td>
    <td align="right">5.65</td>
    <td align="right">5.65</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.51</td>
    <td align="right">6.98</td>
    <td align="right">6.98</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.24</td>
    <td align="right">2.96</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.85</td>
    <td align="right">9.25</td>
    <td align="right">9.26</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.02</td>
    <td align="right">9.66</td>
    <td align="right">9.66</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.75</td>
    <td align="right">2.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.13</td>
    <td align="right">11.77</td>
    <td align="right">11.67</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.12</td>
    <td align="right">13.67</td>
    <td align="right">13.69</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.79</td>
    <td align="right">5.86</td>
    <td align="right">4.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.37</td>
    <td align="right">12.73</td>
    <td align="right">12.74</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.66</td>
    <td align="right">15.14</td>
    <td align="right">15.14</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.83</td>
    <td align="right">5.89</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.18</td>
    <td align="right">2.78</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.65</td>
    <td align="right">4.82</td>
    <td align="right">4.82</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.79</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.34</td>
    <td align="right">2.84</td>
    <td align="right">2.86</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.82</td>
    <td align="right">4.72</td>
    <td align="right">4.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.66</td>
    <td align="right">3.89</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.67</td>
    <td align="right">8.23</td>
    <td align="right">6.16</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.86</td>
    <td align="right">7.98</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.60</td>
    <td align="right">5.68</td>
    <td align="right">3.91</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.49</td>
    <td align="right">9.42</td>
    <td align="right">6.28</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.63</td>
    <td align="right">9.20</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.41</td>
    <td align="right">7.34</td>
    <td align="right">14.49</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.76</td>
    <td align="right">8.84</td>
    <td align="right">18.90</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.16</td>
    <td align="right">11.10</td>
    <td align="right">10.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.40</td>
    <td align="right">14.41</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">10.53</td>
    <td align="right">16.14</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.04</td>
    <td align="right">13.94</td>
    <td align="right">14.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.66</td>
    <td align="right">11.93</td>
    <td align="right">14.09</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.93</td>
    <td align="right">12.94</td>
    <td align="right">17.33</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.18</td>
    <td align="right">16.13</td>
    <td align="right">16.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.88</td>
    <td align="right">14.38</td>
    <td align="right">14.78</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.62</td>
    <td align="right">15.18</td>
    <td align="right">16.81</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.73</td>
    <td align="right">21.09</td>
    <td align="right">21.04</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.41</td>
    <td align="right">23.48</td>
    <td align="right">14.39</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.04</td>
    <td align="right">15.82</td>
    <td align="right">20.84</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.82</td>
    <td align="right">6.50</td>
    <td align="right">6.54</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.46</td>
    <td align="right">6.13</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.65</td>
    <td align="right">52.28</td>
    <td align="right">27.38</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.07</td>
    <td align="right">10.98</td>
    <td align="right">10.98</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.52</td>
    <td align="right">12.52</td>
    <td align="right">12.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.25</td>
    <td align="right">99.75</td>
    <td align="right">34.96</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.34</td>
    <td align="right">18.38</td>
    <td align="right">18.39</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.97</td>
    <td align="right">19.08</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.12</td>
    <td align="right">135.16</td>
    <td align="right">39.56</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.87</td>
    <td align="right">21.99</td>
    <td align="right">21.99</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.85</td>
    <td align="right">25.21</td>
    <td align="right">25.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.42</td>
    <td align="right">7.10</td>
    <td align="right">7.12</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.23</td>
    <td align="right">8.98</td>
    <td align="right">8.96</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">5.90</td>
    <td align="right">5.67</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.45</td>
    <td align="right">17.14</td>
    <td align="right">17.16</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.49</td>
    <td align="right">20.61</td>
    <td align="right">20.65</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.63</td>
    <td align="right">7.92</td>
    <td align="right">7.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.25</td>
    <td align="right">30.26</td>
    <td align="right">30.26</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.90</td>
    <td align="right">35.52</td>
    <td align="right">35.29</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.11</td>
    <td align="right">20.64</td>
    <td align="right">14.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.40</td>
    <td align="right">39.18</td>
    <td align="right">39.20</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.68</td>
    <td align="right">50.85</td>
    <td align="right">50.24</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.00</td>
    <td align="right">23.66</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.24</td>
    <td align="right">3.92</td>
    <td align="right">3.96</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.59</td>
    <td align="right">5.86</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.97</td>
    <td align="right">6.01</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.19</td>
    <td align="right">8.03</td>
    <td align="right">8.03</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.75</td>
    <td align="right">9.69</td>
    <td align="right">9.74</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.13</td>
    <td align="right">12.23</td>
    <td align="right">12.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.60</td>
    <td align="right">20.34</td>
    <td align="right">14.59</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">24.65</td>
    <td align="right">25.86</td>
    <td align="right">21.31</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.72</td>
    <td align="right">26.12</td>
    <td align="right">21.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.80</td>
    <td align="right">23.56</td>
    <td align="right">16.42</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">31.93</td>
    <td align="right">36.25</td>
    <td align="right">24.75</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.64</td>
    <td align="right">36.52</td>
    <td align="right">25.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.58</td>
    <td align="right">8.62</td>
    <td align="right">15.62</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.07</td>
    <td align="right">10.80</td>
    <td align="right">20.72</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.28</td>
    <td align="right">15.27</td>
    <td align="right">15.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.22</td>
    <td align="right">18.44</td>
    <td align="right">18.84</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.19</td>
    <td align="right">21.28</td>
    <td align="right">20.79</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">26.63</td>
    <td align="right">28.35</td>
    <td align="right">28.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.39</td>
    <td align="right">27.86</td>
    <td align="right">21.79</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.48</td>
    <td align="right">33.83</td>
    <td align="right">26.65</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.00</td>
    <td align="right">49.14</td>
    <td align="right">49.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.61</td>
    <td align="right">42.34</td>
    <td align="right">24.90</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.90</td>
    <td align="right">50.31</td>
    <td align="right">28.79</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.41</td>
    <td align="right">73.92</td>
    <td align="right">73.83</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.97</td>
    <td align="right">5.94</td>
    <td align="right">4.27</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.36</td>
    <td align="right">10.83</td>
    <td align="right">18.29</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.06</td>
    <td align="right">4.10</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.06</td>
    <td align="right">4.60</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.71</td>
    <td align="right">16.08</td>
    <td align="right">18.74</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.74</td>
    <td align="right">19.88</td>
    <td align="right">17.47</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.30</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.93</td>
    <td align="right">5.73</td>
    <td align="right">5.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.39</td>
    <td align="right">24.18</td>
    <td align="right">18.01</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.28</td>
    <td align="right">3.90</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.37</td>
    <td align="right">3.68</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.92</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.35</td>
    <td align="right">4.81</td>
    <td align="right">4.81</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.06</td>
    <td align="right">4.94</td>
    <td align="right">4.94</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.78</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.80</td>
    <td align="right">7.74</td>
    <td align="right">7.73</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.98</td>
    <td align="right">7.46</td>
    <td align="right">7.36</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.41</td>
    <td align="right">4.50</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.18</td>
    <td align="right">8.21</td>
    <td align="right">8.23</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.96</td>
    <td align="right">8.38</td>
    <td align="right">8.24</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.46</td>
    <td align="right">4.49</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.85</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.88</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.24</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.50</td>
    <td align="right">4.21</td>
    <td align="right">3.17</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.63</td>
    <td align="right">5.98</td>
    <td align="right">5.18</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.00</td>
    <td align="right">6.08</td>
    <td align="right">4.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.24</td>
    <td align="right">3.14</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.94</td>
    <td align="right">7.27</td>
    <td align="right">5.27</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.24</td>
    <td align="right">7.02</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.32</td>
    <td align="right">6.67</td>
    <td align="right">13.76</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">12.70</td>
    <td align="right">7.88</td>
    <td align="right">18.08</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.39</td>
    <td align="right">10.55</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.62</td>
    <td align="right">9.07</td>
    <td align="right">13.46</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">14.53</td>
    <td align="right">9.28</td>
    <td align="right">15.41</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.74</td>
    <td align="right">13.96</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">12.01</td>
    <td align="right">10.66</td>
    <td align="right">13.54</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.54</td>
    <td align="right">11.97</td>
    <td align="right">16.38</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.86</td>
    <td align="right">16.17</td>
    <td align="right">15.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.30</td>
    <td align="right">13.36</td>
    <td align="right">13.94</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.15</td>
    <td align="right">13.62</td>
    <td align="right">15.78</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.63</td>
    <td align="right">21.10</td>
    <td align="right">21.06</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.13</td>
    <td align="right">23.68</td>
    <td align="right">14.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.57</td>
    <td align="right">14.12</td>
    <td align="right">20.85</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.65</td>
    <td align="right">5.67</td>
    <td align="right">5.63</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.42</td>
    <td align="right">6.03</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.85</td>
    <td align="right">49.49</td>
    <td align="right">26.49</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.03</td>
    <td align="right">10.97</td>
    <td align="right">10.98</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">10.64</td>
    <td align="right">11.56</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.54</td>
    <td align="right">85.35</td>
    <td align="right">31.09</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.89</td>
    <td align="right">17.95</td>
    <td align="right">17.96</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.23</td>
    <td align="right">19.07</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.39</td>
    <td align="right">119.09</td>
    <td align="right">36.47</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.98</td>
    <td align="right">21.72</td>
    <td align="right">21.72</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.71</td>
    <td align="right">15.30</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.32</td>
    <td align="right">5.17</td>
    <td align="right">5.21</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.10</td>
    <td align="right">4.63</td>
    <td align="right">4.66</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.56</td>
    <td align="right">3.45</td>
    <td align="right">3.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.83</td>
    <td align="right">10.55</td>
    <td align="right">10.56</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.91</td>
    <td align="right">12.46</td>
    <td align="right">12.52</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.85</td>
    <td align="right">7.54</td>
    <td align="right">7.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.62</td>
    <td align="right">22.72</td>
    <td align="right">22.75</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.05</td>
    <td align="right">22.93</td>
    <td align="right">22.92</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.19</td>
    <td align="right">16.32</td>
    <td align="right">12.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.87</td>
    <td align="right">29.73</td>
    <td align="right">29.79</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.92</td>
    <td align="right">30.80</td>
    <td align="right">30.80</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.36</td>
    <td align="right">18.34</td>
    <td align="right">13.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.72</td>
    <td align="right">3.38</td>
    <td align="right">3.36</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.76</td>
    <td align="right">5.07</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.27</td>
    <td align="right">5.37</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.60</td>
    <td align="right">7.58</td>
    <td align="right">7.56</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.66</td>
    <td align="right">9.24</td>
    <td align="right">9.27</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.28</td>
    <td align="right">11.52</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.43</td>
    <td align="right">16.09</td>
    <td align="right">11.92</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.19</td>
    <td align="right">21.55</td>
    <td align="right">17.22</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.83</td>
    <td align="right">21.05</td>
    <td align="right">16.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.64</td>
    <td align="right">18.26</td>
    <td align="right">13.45</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.12</td>
    <td align="right">29.48</td>
    <td align="right">20.08</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.37</td>
    <td align="right">26.90</td>
    <td align="right">19.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.67</td>
    <td align="right">7.97</td>
    <td align="right">15.08</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.91</td>
    <td align="right">10.27</td>
    <td align="right">19.76</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.83</td>
    <td align="right">13.87</td>
    <td align="right">13.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.06</td>
    <td align="right">15.61</td>
    <td align="right">17.52</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">25.80</td>
    <td align="right">21.21</td>
    <td align="right">20.63</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.17</td>
    <td align="right">32.58</td>
    <td align="right">32.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.89</td>
    <td align="right">26.74</td>
    <td align="right">21.75</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.21</td>
    <td align="right">32.66</td>
    <td align="right">24.97</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.58</td>
    <td align="right">48.10</td>
    <td align="right">47.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.30</td>
    <td align="right">35.81</td>
    <td align="right">24.25</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.38</td>
    <td align="right">40.08</td>
    <td align="right">26.46</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.06</td>
    <td align="right">72.34</td>
    <td align="right">72.55</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.66</td>
    <td align="right">2.44</td>
    <td align="right">1.98</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.34</td>
    <td align="right">4.16</td>
    <td align="right">11.42</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.32</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.61</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.41</td>
    <td align="right">6.06</td>
    <td align="right">11.99</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.68</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.59</td>
    <td align="right">7.31</td>
    <td align="right">11.21</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.60</td>
    <td align="right">1.63</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.58</td>
    <td align="right">1.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">15.01</td>
    <td align="right">9.39</td>
    <td align="right">11.46</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.28</td>
    <td align="right">1.75</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.25</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.01</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">2.13</td>
    <td align="right">2.13</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.50</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">2.90</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.03</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.88</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.49</td>
    <td align="right">3.36</td>
    <td align="right">3.37</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.78</td>
    <td align="right">3.58</td>
    <td align="right">3.61</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.99</td>
    <td align="right">2.92</td>
    <td align="right">1.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">1.74</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.28</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.05</td>
    <td align="right">1.59</td>
    <td align="right">1.60</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">1.86</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">2.15</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.87</td>
    <td align="right">2.39</td>
    <td align="right">1.75</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.07</td>
    <td align="right">2.90</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.03</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.97</td>
    <td align="right">2.88</td>
    <td align="right">1.73</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.54</td>
    <td align="right">3.37</td>
    <td align="right">3.37</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.79</td>
    <td align="right">3.61</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.23</td>
    <td align="right">3.28</td>
    <td align="right">10.23</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.98</td>
    <td align="right">3.90</td>
    <td align="right">12.75</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.71</td>
    <td align="right">4.89</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.39</td>
    <td align="right">4.38</td>
    <td align="right">10.02</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.45</td>
    <td align="right">4.56</td>
    <td align="right">10.57</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.93</td>
    <td align="right">6.82</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.48</td>
    <td align="right">5.24</td>
    <td align="right">9.74</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.54</td>
    <td align="right">5.77</td>
    <td align="right">11.29</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.04</td>
    <td align="right">7.57</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.05</td>
    <td align="right">6.33</td>
    <td align="right">10.25</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.43</td>
    <td align="right">6.38</td>
    <td align="right">10.80</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.17</td>
    <td align="right">10.67</td>
    <td align="right">10.67</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.36</td>
    <td align="right">10.90</td>
    <td align="right">5.73</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.75</td>
    <td align="right">6.16</td>
    <td align="right">12.93</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.05</td>
    <td align="right">1.99</td>
    <td align="right">2.00</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.13</td>
    <td align="right">2.02</td>
    <td align="right">2.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.15</td>
    <td align="right">11.04</td>
    <td align="right">16.16</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.50</td>
    <td align="right">3.47</td>
    <td align="right">3.49</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.22</td>
    <td align="right">3.16</td>
    <td align="right">3.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">30.88</td>
    <td align="right">24.03</td>
    <td align="right">18.38</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.66</td>
    <td align="right">6.31</td>
    <td align="right">6.56</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.92</td>
    <td align="right">5.98</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.83</td>
    <td align="right">40.29</td>
    <td align="right">20.91</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.13</td>
    <td align="right">7.94</td>
    <td align="right">7.86</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.69</td>
    <td align="right">6.46</td>
    <td align="right">6.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">2.48</td>
    <td align="right">2.56</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.70</td>
    <td align="right">2.59</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.38</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.76</td>
    <td align="right">4.62</td>
    <td align="right">4.28</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.31</td>
    <td align="right">4.64</td>
    <td align="right">4.53</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.75</td>
    <td align="right">3.44</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.95</td>
    <td align="right">9.92</td>
    <td align="right">9.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.68</td>
    <td align="right">9.53</td>
    <td align="right">9.51</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.69</td>
    <td align="right">8.41</td>
    <td align="right">5.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.22</td>
    <td align="right">12.68</td>
    <td align="right">12.37</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.96</td>
    <td align="right">12.90</td>
    <td align="right">12.72</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.43</td>
    <td align="right">11.08</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.39</td>
    <td align="right">2.51</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.72</td>
    <td align="right">2.51</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.71</td>
    <td align="right">2.57</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.94</td>
    <td align="right">3.10</td>
    <td align="right">3.03</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.70</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.26</td>
    <td align="right">4.68</td>
    <td align="right">4.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">8.29</td>
    <td align="right">8.49</td>
    <td align="right">5.82</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.94</td>
    <td align="right">9.88</td>
    <td align="right">9.73</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.28</td>
    <td align="right">9.95</td>
    <td align="right">9.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">10.41</td>
    <td align="right">10.88</td>
    <td align="right">6.60</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">16.00</td>
    <td align="right">12.90</td>
    <td align="right">13.27</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.77</td>
    <td align="right">13.47</td>
    <td align="right">13.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.64</td>
    <td align="right">4.30</td>
    <td align="right">11.29</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.72</td>
    <td align="right">4.92</td>
    <td align="right">13.50</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.87</td>
    <td align="right">6.65</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">9.37</td>
    <td align="right">8.45</td>
    <td align="right">13.03</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.33</td>
    <td align="right">7.80</td>
    <td align="right">12.91</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.57</td>
    <td align="right">12.25</td>
    <td align="right">12.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">16.42</td>
    <td align="right">13.68</td>
    <td align="right">14.25</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">21.98</td>
    <td align="right">15.88</td>
    <td align="right">16.60</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">26.05</td>
    <td align="right">21.96</td>
    <td align="right">23.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">23.13</td>
    <td align="right">17.52</td>
    <td align="right">15.45</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">28.91</td>
    <td align="right">22.21</td>
    <td align="right">17.26</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">49.71</td>
    <td align="right">38.19</td>
    <td align="right">39.07</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.37</td>
    <td align="right">5.19</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.35</td>
    <td align="right">11.37</td>
    <td align="right">14.37</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.61</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.38</td>
    <td align="right">4.15</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.11</td>
    <td align="right">16.16</td>
    <td align="right">14.76</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.43</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.72</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.24</td>
    <td align="right">20.39</td>
    <td align="right">14.24</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.05</td>
    <td align="right">4.38</td>
    <td align="right">4.35</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.69</td>
    <td align="right">5.15</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.89</td>
    <td align="right">25.11</td>
    <td align="right">14.41</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.73</td>
    <td align="right">4.74</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.28</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.41</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.50</td>
    <td align="right">4.65</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.24</td>
    <td align="right">7.00</td>
    <td align="right">6.93</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.70</td>
    <td align="right">7.07</td>
    <td align="right">7.03</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.74</td>
    <td align="right">2.98</td>
    <td align="right">2.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.62</td>
    <td align="right">9.16</td>
    <td align="right">9.05</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.39</td>
    <td align="right">10.45</td>
    <td align="right">10.48</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.28</td>
    <td align="right">4.46</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.69</td>
    <td align="right">10.37</td>
    <td align="right">10.24</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.81</td>
    <td align="right">12.29</td>
    <td align="right">12.14</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.32</td>
    <td align="right">4.46</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.87</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.73</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.79</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.25</td>
    <td align="right">3.37</td>
    <td align="right">2.73</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">3.89</td>
    <td align="right">3.27</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">4.62</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.40</td>
    <td align="right">4.33</td>
    <td align="right">3.04</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.95</td>
    <td align="right">6.39</td>
    <td align="right">5.00</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.72</td>
    <td align="right">6.30</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.40</td>
    <td align="right">4.34</td>
    <td align="right">3.00</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.88</td>
    <td align="right">7.07</td>
    <td align="right">5.10</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.02</td>
    <td align="right">6.85</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.07</td>
    <td align="right">6.73</td>
    <td align="right">11.22</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.04</td>
    <td align="right">8.94</td>
    <td align="right">14.10</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.12</td>
    <td align="right">8.88</td>
    <td align="right">8.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.39</td>
    <td align="right">9.67</td>
    <td align="right">11.91</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.77</td>
    <td align="right">11.21</td>
    <td align="right">13.21</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.62</td>
    <td align="right">12.94</td>
    <td align="right">12.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.39</td>
    <td align="right">11.40</td>
    <td align="right">11.76</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.19</td>
    <td align="right">13.25</td>
    <td align="right">12.71</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.52</td>
    <td align="right">15.35</td>
    <td align="right">15.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.66</td>
    <td align="right">13.86</td>
    <td align="right">12.45</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.37</td>
    <td align="right">15.18</td>
    <td align="right">12.34</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.44</td>
    <td align="right">22.60</td>
    <td align="right">22.58</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.29</td>
    <td align="right">23.34</td>
    <td align="right">12.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.10</td>
    <td align="right">11.87</td>
    <td align="right">15.76</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.21</td>
    <td align="right">3.84</td>
    <td align="right">3.79</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.72</td>
    <td align="right">4.58</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">18.05</td>
    <td align="right">18.04</td>
    <td align="right">16.58</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.22</td>
    <td align="right">5.70</td>
    <td align="right">5.67</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.09</td>
    <td align="right">6.91</td>
    <td align="right">6.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.24</td>
    <td align="right">79.45</td>
    <td align="right">25.94</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.32</td>
    <td align="right">13.98</td>
    <td align="right">13.97</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.42</td>
    <td align="right">16.00</td>
    <td align="right">16.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.36</td>
    <td align="right">117.69</td>
    <td align="right">31.08</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">20.87</td>
    <td align="right">19.33</td>
    <td align="right">19.26</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.70</td>
    <td align="right">22.48</td>
    <td align="right">22.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.10</td>
    <td align="right">4.69</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.57</td>
    <td align="right">5.05</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.17</td>
    <td align="right">2.40</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.18</td>
    <td align="right">8.79</td>
    <td align="right">8.59</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">14.85</td>
    <td align="right">9.56</td>
    <td align="right">9.29</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.81</td>
    <td align="right">4.92</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.70</td>
    <td align="right">23.24</td>
    <td align="right">23.54</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.69</td>
    <td align="right">27.85</td>
    <td align="right">27.90</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.92</td>
    <td align="right">16.50</td>
    <td align="right">11.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.05</td>
    <td align="right">34.93</td>
    <td align="right">35.15</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.81</td>
    <td align="right">38.16</td>
    <td align="right">38.14</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.37</td>
    <td align="right">17.89</td>
    <td align="right">12.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.18</td>
    <td align="right">2.26</td>
    <td align="right">2.16</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.08</td>
    <td align="right">3.48</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.17</td>
    <td align="right">3.40</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.21</td>
    <td align="right">5.56</td>
    <td align="right">4.70</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.73</td>
    <td align="right">6.13</td>
    <td align="right">5.67</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.65</td>
    <td align="right">6.64</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.06</td>
    <td align="right">15.45</td>
    <td align="right">10.99</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.17</td>
    <td align="right">18.49</td>
    <td align="right">15.69</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.82</td>
    <td align="right">19.11</td>
    <td align="right">16.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.74</td>
    <td align="right">17.88</td>
    <td align="right">12.32</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.66</td>
    <td align="right">26.92</td>
    <td align="right">18.97</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.58</td>
    <td align="right">26.87</td>
    <td align="right">19.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.72</td>
    <td align="right">7.43</td>
    <td align="right">11.95</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.68</td>
    <td align="right">9.72</td>
    <td align="right">14.95</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.52</td>
    <td align="right">10.03</td>
    <td align="right">10.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.37</td>
    <td align="right">12.06</td>
    <td align="right">13.71</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.52</td>
    <td align="right">13.96</td>
    <td align="right">14.46</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">15.45</td>
    <td align="right">14.39</td>
    <td align="right">14.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.26</td>
    <td align="right">25.52</td>
    <td align="right">19.68</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.28</td>
    <td align="right">32.53</td>
    <td align="right">20.02</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.18</td>
    <td align="right">40.24</td>
    <td align="right">40.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.58</td>
    <td align="right">34.62</td>
    <td align="right">22.93</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.87</td>
    <td align="right">41.63</td>
    <td align="right">22.03</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.99</td>
    <td align="right">64.79</td>
    <td align="right">64.87</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.85</td>
    <td align="right">34.16</td>
    <td align="right">14.23</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">31.14</td>
    <td align="right">44.70</td>
    <td align="right">37.86</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.35</td>
    <td align="right">16.23</td>
    <td align="right">16.25</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.58</td>
    <td align="right">18.13</td>
    <td align="right">17.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">47.03</td>
    <td align="right">67.46</td>
    <td align="right">40.60</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.35</td>
    <td align="right">18.27</td>
    <td align="right">18.24</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.08</td>
    <td align="right">19.11</td>
    <td align="right">19.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.56</td>
    <td align="right">82.58</td>
    <td align="right">38.96</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.40</td>
    <td align="right">20.48</td>
    <td align="right">20.56</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.07</td>
    <td align="right">21.53</td>
    <td align="right">21.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">73.13</td>
    <td align="right">104.54</td>
    <td align="right">40.79</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.68</td>
    <td align="right">22.19</td>
    <td align="right">22.18</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.54</td>
    <td align="right">22.00</td>
    <td align="right">22.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.86</td>
    <td align="right">23.70</td>
    <td align="right">23.73</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">26.61</td>
    <td align="right">26.54</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.78</td>
    <td align="right">15.98</td>
    <td align="right">15.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.64</td>
    <td align="right">30.11</td>
    <td align="right">30.08</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.00</td>
    <td align="right">34.53</td>
    <td align="right">34.53</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.89</td>
    <td align="right">17.77</td>
    <td align="right">17.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.21</td>
    <td align="right">36.95</td>
    <td align="right">36.90</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.88</td>
    <td align="right">49.04</td>
    <td align="right">49.16</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.04</td>
    <td align="right">20.83</td>
    <td align="right">20.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.68</td>
    <td align="right">41.54</td>
    <td align="right">41.63</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.47</td>
    <td align="right">58.61</td>
    <td align="right">58.58</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.17</td>
    <td align="right">25.90</td>
    <td align="right">25.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.44</td>
    <td align="right">16.86</td>
    <td align="right">16.87</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.93</td>
    <td align="right">23.69</td>
    <td align="right">23.78</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.26</td>
    <td align="right">26.58</td>
    <td align="right">26.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.04</td>
    <td align="right">21.08</td>
    <td align="right">21.19</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.58</td>
    <td align="right">30.00</td>
    <td align="right">30.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.02</td>
    <td align="right">34.54</td>
    <td align="right">34.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.42</td>
    <td align="right">25.06</td>
    <td align="right">25.09</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.37</td>
    <td align="right">37.12</td>
    <td align="right">37.04</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.89</td>
    <td align="right">49.07</td>
    <td align="right">49.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.80</td>
    <td align="right">33.09</td>
    <td align="right">33.09</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.68</td>
    <td align="right">41.71</td>
    <td align="right">41.62</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.45</td>
    <td align="right">58.46</td>
    <td align="right">58.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.33</td>
    <td align="right">24.57</td>
    <td align="right">27.89</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.72</td>
    <td align="right">31.52</td>
    <td align="right">36.23</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.37</td>
    <td align="right">34.77</td>
    <td align="right">34.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.38</td>
    <td align="right">36.80</td>
    <td align="right">28.60</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.32</td>
    <td align="right">40.67</td>
    <td align="right">34.70</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.24</td>
    <td align="right">44.99</td>
    <td align="right">45.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.06</td>
    <td align="right">44.05</td>
    <td align="right">27.98</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.50</td>
    <td align="right">49.82</td>
    <td align="right">36.29</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.97</td>
    <td align="right">47.52</td>
    <td align="right">47.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.28</td>
    <td align="right">49.09</td>
    <td align="right">29.41</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.32</td>
    <td align="right">52.57</td>
    <td align="right">36.02</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.57</td>
    <td align="right">65.82</td>
    <td align="right">65.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.06</td>
    <td align="right">126.21</td>
    <td align="right">27.06</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">38.17</td>
    <td align="right">53.86</td>
    <td align="right">44.47</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.53</td>
    <td align="right">19.80</td>
    <td align="right">19.83</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.40</td>
    <td align="right">20.39</td>
    <td align="right">20.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">94.43</td>
    <td align="right">124.66</td>
    <td align="right">58.54</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.65</td>
    <td align="right">29.05</td>
    <td align="right">28.80</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.74</td>
    <td align="right">31.52</td>
    <td align="right">31.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">191.58</td>
    <td align="right">250.14</td>
    <td align="right">78.47</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.55</td>
    <td align="right">48.24</td>
    <td align="right">48.15</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.58</td>
    <td align="right">47.80</td>
    <td align="right">47.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.79</td>
    <td align="right">432.50</td>
    <td align="right">105.91</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.20</td>
    <td align="right">62.95</td>
    <td align="right">62.93</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.08</td>
    <td align="right">60.76</td>
    <td align="right">60.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.46</td>
    <td align="right">27.54</td>
    <td align="right">27.52</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.58</td>
    <td align="right">29.88</td>
    <td align="right">29.86</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.74</td>
    <td align="right">18.22</td>
    <td align="right">17.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.72</td>
    <td align="right">46.04</td>
    <td align="right">45.94</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">52.59</td>
    <td align="right">50.30</td>
    <td align="right">50.28</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">26.25</td>
    <td align="right">29.40</td>
    <td align="right">29.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.43</td>
    <td align="right">72.27</td>
    <td align="right">72.28</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.65</td>
    <td align="right">83.67</td>
    <td align="right">83.65</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.59</td>
    <td align="right">45.17</td>
    <td align="right">45.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.32</td>
    <td align="right">94.42</td>
    <td align="right">94.61</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.97</td>
    <td align="right">109.09</td>
    <td align="right">109.19</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.19</td>
    <td align="right">75.76</td>
    <td align="right">75.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">17.18</td>
    <td align="right">20.98</td>
    <td align="right">21.28</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">22.80</td>
    <td align="right">27.28</td>
    <td align="right">27.20</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.53</td>
    <td align="right">33.03</td>
    <td align="right">32.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.47</td>
    <td align="right">30.69</td>
    <td align="right">30.87</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.84</td>
    <td align="right">46.57</td>
    <td align="right">46.58</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.26</td>
    <td align="right">51.30</td>
    <td align="right">51.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.38</td>
    <td align="right">56.87</td>
    <td align="right">56.85</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.99</td>
    <td align="right">72.66</td>
    <td align="right">72.62</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.57</td>
    <td align="right">86.01</td>
    <td align="right">85.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.01</td>
    <td align="right">82.97</td>
    <td align="right">82.84</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.05</td>
    <td align="right">94.50</td>
    <td align="right">94.62</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.12</td>
    <td align="right">110.30</td>
    <td align="right">110.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.58</td>
    <td align="right">28.93</td>
    <td align="right">32.16</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.27</td>
    <td align="right">38.06</td>
    <td align="right">41.19</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.06</td>
    <td align="right">38.26</td>
    <td align="right">37.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.97</td>
    <td align="right">50.02</td>
    <td align="right">36.87</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">59.03</td>
    <td align="right">54.71</td>
    <td align="right">44.83</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.33</td>
    <td align="right">66.45</td>
    <td align="right">66.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.45</td>
    <td align="right">73.15</td>
    <td align="right">48.35</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.84</td>
    <td align="right">87.87</td>
    <td align="right">60.10</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">88.65</td>
    <td align="right">93.96</td>
    <td align="right">93.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.57</td>
    <td align="right">90.55</td>
    <td align="right">58.32</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.25</td>
    <td align="right">105.74</td>
    <td align="right">68.25</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.20</td>
    <td align="right">144.08</td>
    <td align="right">142.80</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.86</td>
    <td align="right">13.85</td>
    <td align="right">8.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.49</td>
    <td align="right">28.31</td>
    <td align="right">29.32</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.48</td>
    <td align="right">13.93</td>
    <td align="right">13.94</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.87</td>
    <td align="right">18.10</td>
    <td align="right">18.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.77</td>
    <td align="right">42.86</td>
    <td align="right">31.39</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.03</td>
    <td align="right">18.44</td>
    <td align="right">18.48</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.24</td>
    <td align="right">20.74</td>
    <td align="right">20.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.24</td>
    <td align="right">62.85</td>
    <td align="right">32.45</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.61</td>
    <td align="right">21.35</td>
    <td align="right">21.35</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.05</td>
    <td align="right">22.90</td>
    <td align="right">22.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">61.89</td>
    <td align="right">79.61</td>
    <td align="right">33.53</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">23.26</td>
    <td align="right">23.25</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">25.71</td>
    <td align="right">25.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.06</td>
    <td align="right">18.36</td>
    <td align="right">18.34</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.03</td>
    <td align="right">18.86</td>
    <td align="right">18.85</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.96</td>
    <td align="right">8.72</td>
    <td align="right">8.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.58</td>
    <td align="right">26.52</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">26.93</td>
    <td align="right">26.92</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.99</td>
    <td align="right">13.74</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.22</td>
    <td align="right">35.33</td>
    <td align="right">35.33</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">34.21</td>
    <td align="right">34.44</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.85</td>
    <td align="right">17.79</td>
    <td align="right">17.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.56</td>
    <td align="right">38.34</td>
    <td align="right">38.30</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.40</td>
    <td align="right">41.25</td>
    <td align="right">41.72</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.09</td>
    <td align="right">19.74</td>
    <td align="right">19.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.66</td>
    <td align="right">8.65</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">18.42</td>
    <td align="right">18.31</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.88</td>
    <td align="right">14.10</td>
    <td align="right">14.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.56</td>
    <td align="right">26.51</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">26.93</td>
    <td align="right">26.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.28</td>
    <td align="right">17.20</td>
    <td align="right">17.25</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.15</td>
    <td align="right">35.25</td>
    <td align="right">35.26</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.55</td>
    <td align="right">34.18</td>
    <td align="right">34.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">20.00</td>
    <td align="right">20.00</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.27</td>
    <td align="right">38.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.44</td>
    <td align="right">41.63</td>
    <td align="right">41.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.26</td>
    <td align="right">20.94</td>
    <td align="right">24.58</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.63</td>
    <td align="right">41.98</td>
    <td align="right">41.89</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">32.53</td>
    <td align="right">27.21</td>
    <td align="right">28.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.01</td>
    <td align="right">29.75</td>
    <td align="right">24.22</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.90</td>
    <td align="right">46.32</td>
    <td align="right">39.38</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.78</td>
    <td align="right">36.74</td>
    <td align="right">36.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.18</td>
    <td align="right">35.75</td>
    <td align="right">24.47</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">61.81</td>
    <td align="right">53.89</td>
    <td align="right">40.19</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.56</td>
    <td align="right">38.73</td>
    <td align="right">38.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.75</td>
    <td align="right">46.87</td>
    <td align="right">30.08</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.79</td>
    <td align="right">58.91</td>
    <td align="right">43.75</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.35</td>
    <td align="right">50.90</td>
    <td align="right">50.23</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">123.70</td>
    <td align="right">61.73</td>
    <td align="right">23.04</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.45</td>
    <td align="right">34.75</td>
    <td align="right">34.06</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">13.40</td>
    <td align="right">14.88</td>
    <td align="right">14.89</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.33</td>
    <td align="right">21.52</td>
    <td align="right">21.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">80.43</td>
    <td align="right">98.40</td>
    <td align="right">47.41</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.72</td>
    <td align="right">27.31</td>
    <td align="right">27.19</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.53</td>
    <td align="right">33.81</td>
    <td align="right">33.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">146.31</td>
    <td align="right">206.19</td>
    <td align="right">66.05</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.17</td>
    <td align="right">49.61</td>
    <td align="right">49.52</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.77</td>
    <td align="right">50.62</td>
    <td align="right">50.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.10</td>
    <td align="right">299.27</td>
    <td align="right">83.51</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.56</td>
    <td align="right">65.35</td>
    <td align="right">65.34</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.25</td>
    <td align="right">70.34</td>
    <td align="right">70.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.12</td>
    <td align="right">20.75</td>
    <td align="right">20.75</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.89</td>
    <td align="right">22.46</td>
    <td align="right">22.46</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.51</td>
    <td align="right">11.79</td>
    <td align="right">11.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.76</td>
    <td align="right">37.85</td>
    <td align="right">37.66</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.59</td>
    <td align="right">43.31</td>
    <td align="right">43.39</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">19.50</td>
    <td align="right">21.16</td>
    <td align="right">21.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.80</td>
    <td align="right">69.80</td>
    <td align="right">71.25</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.20</td>
    <td align="right">68.71</td>
    <td align="right">68.46</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.51</td>
    <td align="right">40.44</td>
    <td align="right">40.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.86</td>
    <td align="right">90.00</td>
    <td align="right">89.03</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.19</td>
    <td align="right">92.43</td>
    <td align="right">92.69</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.41</td>
    <td align="right">52.24</td>
    <td align="right">52.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.25</td>
    <td align="right">10.23</td>
    <td align="right">10.30</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.20</td>
    <td align="right">21.98</td>
    <td align="right">21.94</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.39</td>
    <td align="right">21.39</td>
    <td align="right">21.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.50</td>
    <td align="right">25.27</td>
    <td align="right">25.31</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.86</td>
    <td align="right">41.26</td>
    <td align="right">41.14</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.05</td>
    <td align="right">44.17</td>
    <td align="right">44.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.40</td>
    <td align="right">41.39</td>
    <td align="right">41.53</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.71</td>
    <td align="right">67.23</td>
    <td align="right">67.25</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.03</td>
    <td align="right">67.58</td>
    <td align="right">67.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.25</td>
    <td align="right">53.32</td>
    <td align="right">53.20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.90</td>
    <td align="right">86.22</td>
    <td align="right">86.23</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.92</td>
    <td align="right">94.20</td>
    <td align="right">94.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">19.84</td>
    <td align="right">22.97</td>
    <td align="right">25.97</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.25</td>
    <td align="right">43.61</td>
    <td align="right">43.33</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.86</td>
    <td align="right">31.92</td>
    <td align="right">31.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.52</td>
    <td align="right">41.20</td>
    <td align="right">31.44</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">65.85</td>
    <td align="right">61.28</td>
    <td align="right">51.07</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">57.82</td>
    <td align="right">57.23</td>
    <td align="right">57.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.65</td>
    <td align="right">64.95</td>
    <td align="right">41.02</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.76</td>
    <td align="right">86.87</td>
    <td align="right">63.15</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.47</td>
    <td align="right">81.83</td>
    <td align="right">81.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.05</td>
    <td align="right">88.92</td>
    <td align="right">57.30</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">110.24</td>
    <td align="right">107.16</td>
    <td align="right">78.25</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.65</td>
    <td align="right">117.67</td>
    <td align="right">117.31</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.06</td>
    <td align="right">6.80</td>
    <td align="right">5.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.67</td>
    <td align="right">60.37</td>
    <td align="right">41.03</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.97</td>
    <td align="right">20.67</td>
    <td align="right">23.34</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.06</td>
    <td align="right">25.19</td>
    <td align="right">26.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.38</td>
    <td align="right">87.31</td>
    <td align="right">42.25</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.32</td>
    <td align="right">22.25</td>
    <td align="right">24.30</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.52</td>
    <td align="right">27.94</td>
    <td align="right">28.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">123.35</td>
    <td align="right">105.20</td>
    <td align="right">41.13</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.15</td>
    <td align="right">25.28</td>
    <td align="right">25.83</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.09</td>
    <td align="right">30.19</td>
    <td align="right">30.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">162.99</td>
    <td align="right">135.65</td>
    <td align="right">41.76</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.65</td>
    <td align="right">26.89</td>
    <td align="right">27.36</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.33</td>
    <td align="right">31.92</td>
    <td align="right">32.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.50</td>
    <td align="right">41.66</td>
    <td align="right">41.60</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.56</td>
    <td align="right">41.44</td>
    <td align="right">41.05</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.60</td>
    <td align="right">28.44</td>
    <td align="right">28.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.54</td>
    <td align="right">55.48</td>
    <td align="right">56.37</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.31</td>
    <td align="right">55.99</td>
    <td align="right">56.46</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.91</td>
    <td align="right">37.62</td>
    <td align="right">27.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.05</td>
    <td align="right">76.72</td>
    <td align="right">75.56</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.43</td>
    <td align="right">75.48</td>
    <td align="right">75.41</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.20</td>
    <td align="right">54.06</td>
    <td align="right">37.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.30</td>
    <td align="right">83.94</td>
    <td align="right">84.48</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">46.84</td>
    <td align="right">89.59</td>
    <td align="right">90.82</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.14</td>
    <td align="right">54.26</td>
    <td align="right">37.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.94</td>
    <td align="right">28.23</td>
    <td align="right">27.82</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.81</td>
    <td align="right">30.64</td>
    <td align="right">30.62</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.39</td>
    <td align="right">30.72</td>
    <td align="right">30.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.09</td>
    <td align="right">44.37</td>
    <td align="right">34.94</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.94</td>
    <td align="right">38.87</td>
    <td align="right">29.03</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.74</td>
    <td align="right">46.79</td>
    <td align="right">37.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.08</td>
    <td align="right">53.58</td>
    <td align="right">36.77</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.84</td>
    <td align="right">57.77</td>
    <td align="right">40.14</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.68</td>
    <td align="right">57.47</td>
    <td align="right">39.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.09</td>
    <td align="right">53.95</td>
    <td align="right">37.21</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.61</td>
    <td align="right">59.41</td>
    <td align="right">40.10</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.94</td>
    <td align="right">59.12</td>
    <td align="right">40.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.01</td>
    <td align="right">43.73</td>
    <td align="right">33.33</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.66</td>
    <td align="right">55.18</td>
    <td align="right">37.21</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.46</td>
    <td align="right">60.82</td>
    <td align="right">60.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.58</td>
    <td align="right">61.61</td>
    <td align="right">33.39</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.76</td>
    <td align="right">61.59</td>
    <td align="right">36.54</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.95</td>
    <td align="right">78.40</td>
    <td align="right">79.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.75</td>
    <td align="right">75.89</td>
    <td align="right">34.79</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.90</td>
    <td align="right">80.10</td>
    <td align="right">36.74</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.67</td>
    <td align="right">83.75</td>
    <td align="right">83.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.70</td>
    <td align="right">99.81</td>
    <td align="right">34.05</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">56.06</td>
    <td align="right">99.59</td>
    <td align="right">36.51</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.98</td>
    <td align="right">115.87</td>
    <td align="right">116.31</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.26</td>
    <td align="right">33.26</td>
    <td align="right">17.19</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">70.17</td>
    <td align="right">62.53</td>
    <td align="right">42.54</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.06</td>
    <td align="right">20.61</td>
    <td align="right">23.99</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.77</td>
    <td align="right">27.00</td>
    <td align="right">28.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">125.88</td>
    <td align="right">112.63</td>
    <td align="right">49.94</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.57</td>
    <td align="right">23.84</td>
    <td align="right">26.09</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">31.07</td>
    <td align="right">30.41</td>
    <td align="right">30.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">258.04</td>
    <td align="right">220.66</td>
    <td align="right">64.44</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.39</td>
    <td align="right">37.09</td>
    <td align="right">37.87</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.53</td>
    <td align="right">48.83</td>
    <td align="right">47.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">433.93</td>
    <td align="right">354.56</td>
    <td align="right">79.21</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.10</td>
    <td align="right">44.94</td>
    <td align="right">45.39</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.69</td>
    <td align="right">62.99</td>
    <td align="right">63.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.56</td>
    <td align="right">41.64</td>
    <td align="right">41.53</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.53</td>
    <td align="right">41.52</td>
    <td align="right">41.24</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.12</td>
    <td align="right">30.30</td>
    <td align="right">30.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.75</td>
    <td align="right">57.00</td>
    <td align="right">57.86</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">36.78</td>
    <td align="right">57.41</td>
    <td align="right">58.01</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.17</td>
    <td align="right">40.17</td>
    <td align="right">30.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.91</td>
    <td align="right">89.78</td>
    <td align="right">88.83</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.35</td>
    <td align="right">91.89</td>
    <td align="right">92.03</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">47.14</td>
    <td align="right">78.15</td>
    <td align="right">61.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">74.92</td>
    <td align="right">106.78</td>
    <td align="right">107.52</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.90</td>
    <td align="right">118.22</td>
    <td align="right">119.65</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.67</td>
    <td align="right">90.18</td>
    <td align="right">74.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.18</td>
    <td align="right">29.88</td>
    <td align="right">29.87</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.12</td>
    <td align="right">31.95</td>
    <td align="right">31.95</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.56</td>
    <td align="right">31.82</td>
    <td align="right">31.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.60</td>
    <td align="right">48.05</td>
    <td align="right">38.29</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.80</td>
    <td align="right">42.69</td>
    <td align="right">33.00</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">22.90</td>
    <td align="right">57.78</td>
    <td align="right">48.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.08</td>
    <td align="right">79.07</td>
    <td align="right">62.99</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.29</td>
    <td align="right">80.57</td>
    <td align="right">63.09</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.78</td>
    <td align="right">81.78</td>
    <td align="right">63.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.20</td>
    <td align="right">92.65</td>
    <td align="right">75.63</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.28</td>
    <td align="right">97.57</td>
    <td align="right">77.61</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.83</td>
    <td align="right">97.95</td>
    <td align="right">78.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.74</td>
    <td align="right">43.97</td>
    <td align="right">35.08</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.36</td>
    <td align="right">55.61</td>
    <td align="right">39.33</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.61</td>
    <td align="right">61.46</td>
    <td align="right">61.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.52</td>
    <td align="right">65.35</td>
    <td align="right">38.04</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">45.46</td>
    <td align="right">63.68</td>
    <td align="right">39.27</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">50.91</td>
    <td align="right">83.81</td>
    <td align="right">85.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">58.00</td>
    <td align="right">88.29</td>
    <td align="right">51.15</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.91</td>
    <td align="right">100.19</td>
    <td align="right">58.83</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">76.74</td>
    <td align="right">102.25</td>
    <td align="right">101.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">78.84</td>
    <td align="right">120.56</td>
    <td align="right">61.16</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.67</td>
    <td align="right">132.24</td>
    <td align="right">72.17</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.20</td>
    <td align="right">143.31</td>
    <td align="right">143.72</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
