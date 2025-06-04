# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
    <td align="right">26.35</td>
    <td align="right">4.67</td>
    <td align="right">3.85</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1635</td>
    <td align="right">11.28</td>
    <td align="right">9.52</td>
    <td align="right">16.32</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.10</td>
    <td align="right">4.22</td>
    <td align="right">9.87</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.91</td>
    <td align="right">5.10</td>
    <td align="right">11.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.16</td>
    <td align="right">13.58</td>
    <td align="right">17.70</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.84</td>
    <td align="right">5.16</td>
    <td align="right">8.00</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.51</td>
    <td align="right">5.92</td>
    <td align="right">9.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.10</td>
    <td align="right">16.37</td>
    <td align="right">16.22</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.54</td>
    <td align="right">5.69</td>
    <td align="right">7.71</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.31</td>
    <td align="right">6.52</td>
    <td align="right">8.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">28.69</td>
    <td align="right">20.70</td>
    <td align="right">16.56</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.23</td>
    <td align="right">6.57</td>
    <td align="right">7.17</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.74</td>
    <td align="right">7.42</td>
    <td align="right">8.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">5.12</td>
    <td align="right">5.81</td>
    <td align="right">5.76</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.29</td>
    <td align="right">6.63</td>
    <td align="right">6.59</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.02</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.68</td>
    <td align="right">8.91</td>
    <td align="right">8.88</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.20</td>
    <td align="right">9.93</td>
    <td align="right">9.91</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.50</td>
    <td align="right">3.00</td>
    <td align="right">2.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.32</td>
    <td align="right">13.87</td>
    <td align="right">13.83</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.81</td>
    <td align="right">14.23</td>
    <td align="right">14.27</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.77</td>
    <td align="right">5.86</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.11</td>
    <td align="right">15.54</td>
    <td align="right">15.50</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.24</td>
    <td align="right">17.56</td>
    <td align="right">17.46</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.82</td>
    <td align="right">5.85</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">2.95</td>
    <td align="right">3.26</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.40</td>
    <td align="right">5.12</td>
    <td align="right">5.04</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.60</td>
    <td align="right">5.02</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.09</td>
    <td align="right">3.38</td>
    <td align="right">3.38</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.20</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.52</td>
    <td align="right">5.14</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.45</td>
    <td align="right">5.59</td>
    <td align="right">3.87</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.14</td>
    <td align="right">7.81</td>
    <td align="right">5.97</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.00</td>
    <td align="right">7.67</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.53</td>
    <td align="right">5.57</td>
    <td align="right">3.82</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.14</td>
    <td align="right">9.23</td>
    <td align="right">6.03</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.46</td>
    <td align="right">9.17</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">6.86</td>
    <td align="right">6.54</td>
    <td align="right">12.76</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.94</td>
    <td align="right">6.43</td>
    <td align="right">12.94</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.53</td>
    <td align="right">8.91</td>
    <td align="right">16.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.35</td>
    <td align="right">8.75</td>
    <td align="right">12.48</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.44</td>
    <td align="right">8.79</td>
    <td align="right">12.56</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.24</td>
    <td align="right">10.10</td>
    <td align="right">14.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.81</td>
    <td align="right">10.89</td>
    <td align="right">12.13</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.03</td>
    <td align="right">10.91</td>
    <td align="right">12.14</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.50</td>
    <td align="right">13.19</td>
    <td align="right">15.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.33</td>
    <td align="right">13.39</td>
    <td align="right">12.75</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.56</td>
    <td align="right">13.45</td>
    <td align="right">12.93</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.95</td>
    <td align="right">15.03</td>
    <td align="right">15.03</td>
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
    <td align="right">32.32</td>
    <td align="right">18.75</td>
    <td align="right">7.60</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1566</td>
    <td align="right">13.98</td>
    <td align="right">11.22</td>
    <td align="right">17.46</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.95</td>
    <td align="right">5.02</td>
    <td align="right">10.36</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.16</td>
    <td align="right">6.20</td>
    <td align="right">11.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.49</td>
    <td align="right">16.03</td>
    <td align="right">19.04</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.51</td>
    <td align="right">6.50</td>
    <td align="right">8.46</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.29</td>
    <td align="right">6.49</td>
    <td align="right">10.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">34.88</td>
    <td align="right">34.63</td>
    <td align="right">19.13</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.72</td>
    <td align="right">8.07</td>
    <td align="right">9.01</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.54</td>
    <td align="right">12.66</td>
    <td align="right">10.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">67.32</td>
    <td align="right">54.40</td>
    <td align="right">22.37</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.39</td>
    <td align="right">13.51</td>
    <td align="right">9.88</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.61</td>
    <td align="right">16.34</td>
    <td align="right">10.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">6.03</td>
    <td align="right">6.87</td>
    <td align="right">6.80</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.26</td>
    <td align="right">7.93</td>
    <td align="right">8.18</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.53</td>
    <td align="right">4.04</td>
    <td align="right">4.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.26</td>
    <td align="right">10.78</td>
    <td align="right">9.90</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.94</td>
    <td align="right">11.54</td>
    <td align="right">11.32</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.14</td>
    <td align="right">3.86</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.16</td>
    <td align="right">15.05</td>
    <td align="right">14.53</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.17</td>
    <td align="right">16.80</td>
    <td align="right">16.80</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.50</td>
    <td align="right">8.25</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">17.77</td>
    <td align="right">25.89</td>
    <td align="right">24.60</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.60</td>
    <td align="right">28.54</td>
    <td align="right">26.98</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">15.62</td>
    <td align="right">15.48</td>
    <td align="right">10.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">3.33</td>
    <td align="right">3.69</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.19</td>
    <td align="right">6.62</td>
    <td align="right">6.36</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.21</td>
    <td align="right">5.76</td>
    <td align="right">6.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">4.45</td>
    <td align="right">5.59</td>
    <td align="right">4.78</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">4.23</td>
    <td align="right">5.68</td>
    <td align="right">5.18</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.09</td>
    <td align="right">6.34</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">10.15</td>
    <td align="right">8.74</td>
    <td align="right">6.67</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">11.37</td>
    <td align="right">12.78</td>
    <td align="right">9.37</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.06</td>
    <td align="right">14.08</td>
    <td align="right">9.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">13.51</td>
    <td align="right">14.95</td>
    <td align="right">10.60</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">20.31</td>
    <td align="right">25.86</td>
    <td align="right">12.65</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">15.54</td>
    <td align="right">21.17</td>
    <td align="right">17.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">8.40</td>
    <td align="right">7.82</td>
    <td align="right">13.48</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.37</td>
    <td align="right">7.69</td>
    <td align="right">13.40</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.90</td>
    <td align="right">10.03</td>
    <td align="right">18.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">12.44</td>
    <td align="right">13.68</td>
    <td align="right">13.45</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.49</td>
    <td align="right">13.20</td>
    <td align="right">13.70</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">17.40</td>
    <td align="right">12.01</td>
    <td align="right">14.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.73</td>
    <td align="right">14.49</td>
    <td align="right">15.02</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.64</td>
    <td align="right">22.66</td>
    <td align="right">14.27</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">23.83</td>
    <td align="right">18.71</td>
    <td align="right">17.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">31.84</td>
    <td align="right">39.02</td>
    <td align="right">17.28</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">27.91</td>
    <td align="right">23.82</td>
    <td align="right">18.22</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">38.82</td>
    <td align="right">32.33</td>
    <td align="right">21.65</td>
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
    <td align="right">26.54</td>
    <td align="right">4.32</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1635</td>
    <td align="right">9.41</td>
    <td align="right">9.00</td>
    <td align="right">15.47</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.34</td>
    <td align="right">5.85</td>
    <td align="right">5.19</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.96</td>
    <td align="right">7.12</td>
    <td align="right">6.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.00</td>
    <td align="right">13.48</td>
    <td align="right">16.62</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.84</td>
    <td align="right">7.13</td>
    <td align="right">7.09</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.49</td>
    <td align="right">8.77</td>
    <td align="right">8.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.40</td>
    <td align="right">16.58</td>
    <td align="right">15.68</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.34</td>
    <td align="right">8.83</td>
    <td align="right">8.84</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.97</td>
    <td align="right">10.15</td>
    <td align="right">10.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.73</td>
    <td align="right">19.36</td>
    <td align="right">15.15</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.81</td>
    <td align="right">10.17</td>
    <td align="right">10.20</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.96</td>
    <td align="right">10.96</td>
    <td align="right">10.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">3.06</td>
    <td align="right">3.63</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.22</td>
    <td align="right">3.53</td>
    <td align="right">3.55</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.59</td>
    <td align="right">2.51</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.73</td>
    <td align="right">4.10</td>
    <td align="right">4.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.79</td>
    <td align="right">4.49</td>
    <td align="right">4.51</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.15</td>
    <td align="right">2.33</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.63</td>
    <td align="right">7.20</td>
    <td align="right">7.26</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.77</td>
    <td align="right">7.00</td>
    <td align="right">7.04</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.24</td>
    <td align="right">4.42</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.02</td>
    <td align="right">7.59</td>
    <td align="right">7.65</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.36</td>
    <td align="right">8.09</td>
    <td align="right">8.19</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.24</td>
    <td align="right">4.41</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">2.62</td>
    <td align="right">2.39</td>
    <td align="right">2.38</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.65</td>
    <td align="right">4.09</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.77</td>
    <td align="right">4.01</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.72</td>
    <td align="right">2.44</td>
    <td align="right">2.44</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.98</td>
    <td align="right">3.79</td>
    <td align="right">3.78</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.92</td>
    <td align="right">4.10</td>
    <td align="right">4.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.29</td>
    <td align="right">4.37</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.13</td>
    <td align="right">6.06</td>
    <td align="right">4.68</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.89</td>
    <td align="right">6.08</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.33</td>
    <td align="right">4.40</td>
    <td align="right">3.54</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.31</td>
    <td align="right">7.15</td>
    <td align="right">4.90</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.80</td>
    <td align="right">7.08</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">6.73</td>
    <td align="right">6.18</td>
    <td align="right">12.43</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.76</td>
    <td align="right">6.17</td>
    <td align="right">12.28</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.31</td>
    <td align="right">7.96</td>
    <td align="right">16.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.35</td>
    <td align="right">8.51</td>
    <td align="right">12.38</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.51</td>
    <td align="right">8.21</td>
    <td align="right">12.23</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.31</td>
    <td align="right">9.64</td>
    <td align="right">13.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.94</td>
    <td align="right">10.24</td>
    <td align="right">12.10</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.69</td>
    <td align="right">10.16</td>
    <td align="right">11.94</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.47</td>
    <td align="right">12.57</td>
    <td align="right">14.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.86</td>
    <td align="right">12.57</td>
    <td align="right">12.88</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.95</td>
    <td align="right">12.37</td>
    <td align="right">12.82</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.94</td>
    <td align="right">14.11</td>
    <td align="right">14.53</td>
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
    <td align="right">33.80</td>
    <td align="right">17.34</td>
    <td align="right">7.69</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1566</td>
    <td align="right">10.95</td>
    <td align="right">10.86</td>
    <td align="right">16.39</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.99</td>
    <td align="right">6.95</td>
    <td align="right">6.03</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.54</td>
    <td align="right">8.25</td>
    <td align="right">7.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.39</td>
    <td align="right">17.62</td>
    <td align="right">17.36</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.47</td>
    <td align="right">8.67</td>
    <td align="right">8.30</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.15</td>
    <td align="right">9.78</td>
    <td align="right">9.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.85</td>
    <td align="right">26.81</td>
    <td align="right">19.07</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.72</td>
    <td align="right">12.46</td>
    <td align="right">12.57</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.18</td>
    <td align="right">15.73</td>
    <td align="right">14.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">48.86</td>
    <td align="right">38.37</td>
    <td align="right">17.75</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.20</td>
    <td align="right">13.98</td>
    <td align="right">14.83</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">6.58</td>
    <td align="right">19.99</td>
    <td align="right">20.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">3.61</td>
    <td align="right">4.23</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.67</td>
    <td align="right">4.12</td>
    <td align="right">4.15</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.08</td>
    <td align="right">3.05</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.24</td>
    <td align="right">4.61</td>
    <td align="right">4.98</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.18</td>
    <td align="right">5.02</td>
    <td align="right">5.16</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.52</td>
    <td align="right">2.69</td>
    <td align="right">2.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.20</td>
    <td align="right">10.78</td>
    <td align="right">11.43</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">8.21</td>
    <td align="right">10.94</td>
    <td align="right">11.24</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.61</td>
    <td align="right">10.75</td>
    <td align="right">6.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.35</td>
    <td align="right">15.95</td>
    <td align="right">18.04</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">11.78</td>
    <td align="right">18.04</td>
    <td align="right">17.38</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.00</td>
    <td align="right">13.64</td>
    <td align="right">9.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">3.05</td>
    <td align="right">2.89</td>
    <td align="right">2.89</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.29</td>
    <td align="right">4.84</td>
    <td align="right">4.85</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.29</td>
    <td align="right">4.81</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.18</td>
    <td align="right">3.08</td>
    <td align="right">3.03</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.69</td>
    <td align="right">4.38</td>
    <td align="right">4.45</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.56</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.20</td>
    <td align="right">5.67</td>
    <td align="right">3.82</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.92</td>
    <td align="right">7.81</td>
    <td align="right">6.49</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.12</td>
    <td align="right">7.77</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.20</td>
    <td align="right">14.49</td>
    <td align="right">9.52</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">11.31</td>
    <td align="right">11.46</td>
    <td align="right">10.44</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.97</td>
    <td align="right">13.05</td>
    <td align="right">8.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">7.72</td>
    <td align="right">7.08</td>
    <td align="right">13.71</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.84</td>
    <td align="right">7.07</td>
    <td align="right">12.80</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.94</td>
    <td align="right">9.14</td>
    <td align="right">16.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.70</td>
    <td align="right">9.85</td>
    <td align="right">14.33</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.89</td>
    <td align="right">10.49</td>
    <td align="right">14.20</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.65</td>
    <td align="right">11.41</td>
    <td align="right">15.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">18.39</td>
    <td align="right">17.09</td>
    <td align="right">15.37</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">18.04</td>
    <td align="right">15.60</td>
    <td align="right">14.60</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">28.23</td>
    <td align="right">22.20</td>
    <td align="right">19.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">43.39</td>
    <td align="right">27.66</td>
    <td align="right">18.58</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">42.71</td>
    <td align="right">36.44</td>
    <td align="right">21.19</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">60.92</td>
    <td align="right">42.35</td>
    <td align="right">22.76</td>
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
    <td align="right">21.27</td>
    <td align="right">4.41</td>
    <td align="right">3.45</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1635</td>
    <td align="right">7.33</td>
    <td align="right">5.05</td>
    <td align="right">13.69</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.43</td>
    <td align="right">2.36</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.74</td>
    <td align="right">2.34</td>
    <td align="right">2.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.80</td>
    <td align="right">7.63</td>
    <td align="right">12.92</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.52</td>
    <td align="right">2.80</td>
    <td align="right">2.57</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.82</td>
    <td align="right">2.75</td>
    <td align="right">2.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.21</td>
    <td align="right">9.75</td>
    <td align="right">12.09</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.78</td>
    <td align="right">3.11</td>
    <td align="right">3.41</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.81</td>
    <td align="right">3.21</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.52</td>
    <td align="right">15.26</td>
    <td align="right">12.96</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.27</td>
    <td align="right">3.94</td>
    <td align="right">3.64</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.43</td>
    <td align="right">4.42</td>
    <td align="right">3.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">2.65</td>
    <td align="right">1.88</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.40</td>
    <td align="right">2.13</td>
    <td align="right">1.98</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.29</td>
    <td align="right">1.89</td>
    <td align="right">1.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.27</td>
    <td align="right">2.74</td>
    <td align="right">2.31</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.97</td>
    <td align="right">2.57</td>
    <td align="right">2.43</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.89</td>
    <td align="right">1.59</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.55</td>
    <td align="right">3.36</td>
    <td align="right">3.86</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.59</td>
    <td align="right">3.58</td>
    <td align="right">3.24</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.53</td>
    <td align="right">2.75</td>
    <td align="right">1.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.12</td>
    <td align="right">3.89</td>
    <td align="right">3.83</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.28</td>
    <td align="right">4.38</td>
    <td align="right">4.59</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.27</td>
    <td align="right">3.36</td>
    <td align="right">1.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">2.19</td>
    <td align="right">1.88</td>
    <td align="right">1.94</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.49</td>
    <td align="right">1.97</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.62</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.25</td>
    <td align="right">1.83</td>
    <td align="right">1.79</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.46</td>
    <td align="right">2.20</td>
    <td align="right">2.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.00</td>
    <td align="right">2.50</td>
    <td align="right">2.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.20</td>
    <td align="right">2.85</td>
    <td align="right">1.96</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.53</td>
    <td align="right">3.20</td>
    <td align="right">3.21</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.49</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.30</td>
    <td align="right">3.28</td>
    <td align="right">2.00</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.30</td>
    <td align="right">4.00</td>
    <td align="right">4.09</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.42</td>
    <td align="right">4.40</td>
    <td align="right">4.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">3.84</td>
    <td align="right">3.95</td>
    <td align="right">11.51</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.66</td>
    <td align="right">3.63</td>
    <td align="right">11.90</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.89</td>
    <td align="right">4.50</td>
    <td align="right">13.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">7.54</td>
    <td align="right">5.26</td>
    <td align="right">11.37</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.07</td>
    <td align="right">5.29</td>
    <td align="right">11.27</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">8.44</td>
    <td align="right">5.29</td>
    <td align="right">11.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">7.10</td>
    <td align="right">7.38</td>
    <td align="right">11.20</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">8.13</td>
    <td align="right">7.35</td>
    <td align="right">11.54</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">10.35</td>
    <td align="right">6.79</td>
    <td align="right">13.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">10.00</td>
    <td align="right">11.34</td>
    <td align="right">14.27</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">11.37</td>
    <td align="right">8.58</td>
    <td align="right">13.14</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.15</td>
    <td align="right">8.15</td>
    <td align="right">13.85</td>
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
    <td align="right">34.40</td>
    <td align="right">14.06</td>
    <td align="right">10.39</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1566</td>
    <td align="right">11.06</td>
    <td align="right">10.92</td>
    <td align="right">21.13</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.43</td>
    <td align="right">8.67</td>
    <td align="right">8.15</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.84</td>
    <td align="right">4.99</td>
    <td align="right">5.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.56</td>
    <td align="right">26.47</td>
    <td align="right">25.05</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.49</td>
    <td align="right">13.03</td>
    <td align="right">11.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.38</td>
    <td align="right">10.95</td>
    <td align="right">11.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">59.77</td>
    <td align="right">38.47</td>
    <td align="right">22.82</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.47</td>
    <td align="right">11.28</td>
    <td align="right">14.36</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.89</td>
    <td align="right">15.05</td>
    <td align="right">14.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">84.24</td>
    <td align="right">66.40</td>
    <td align="right">29.05</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.64</td>
    <td align="right">18.15</td>
    <td align="right">19.32</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.00</td>
    <td align="right">17.19</td>
    <td align="right">16.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">5.24</td>
    <td align="right">5.47</td>
    <td align="right">6.45</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.86</td>
    <td align="right">6.45</td>
    <td align="right">5.93</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.27</td>
    <td align="right">7.99</td>
    <td align="right">5.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.91</td>
    <td align="right">13.07</td>
    <td align="right">13.97</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.87</td>
    <td align="right">14.26</td>
    <td align="right">14.82</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">8.27</td>
    <td align="right">11.46</td>
    <td align="right">10.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">21.32</td>
    <td align="right">14.86</td>
    <td align="right">16.78</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.66</td>
    <td align="right">19.69</td>
    <td align="right">20.13</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">17.98</td>
    <td align="right">15.33</td>
    <td align="right">10.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">28.23</td>
    <td align="right">26.17</td>
    <td align="right">24.93</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.28</td>
    <td align="right">30.20</td>
    <td align="right">27.82</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">20.08</td>
    <td align="right">23.42</td>
    <td align="right">12.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">7.40</td>
    <td align="right">7.67</td>
    <td align="right">7.87</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.60</td>
    <td align="right">5.47</td>
    <td align="right">5.91</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.31</td>
    <td align="right">5.56</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.36</td>
    <td align="right">8.34</td>
    <td align="right">6.95</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.73</td>
    <td align="right">9.87</td>
    <td align="right">9.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.11</td>
    <td align="right">12.66</td>
    <td align="right">14.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.85</td>
    <td align="right">13.71</td>
    <td align="right">10.63</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">20.47</td>
    <td align="right">17.96</td>
    <td align="right">18.58</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">21.23</td>
    <td align="right">17.97</td>
    <td align="right">18.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">18.35</td>
    <td align="right">22.04</td>
    <td align="right">14.55</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">29.63</td>
    <td align="right">26.83</td>
    <td align="right">29.03</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">31.70</td>
    <td align="right">31.75</td>
    <td align="right">30.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">23.69</td>
    <td align="right">21.58</td>
    <td align="right">23.03</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">17.47</td>
    <td align="right">18.28</td>
    <td align="right">28.36</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">30.59</td>
    <td align="right">17.37</td>
    <td align="right">28.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">24.74</td>
    <td align="right">22.35</td>
    <td align="right">19.78</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">16.03</td>
    <td align="right">16.38</td>
    <td align="right">17.93</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">48.48</td>
    <td align="right">28.68</td>
    <td align="right">28.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">38.81</td>
    <td align="right">28.74</td>
    <td align="right">20.08</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">29.05</td>
    <td align="right">29.20</td>
    <td align="right">24.13</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">40.83</td>
    <td align="right">21.90</td>
    <td align="right">21.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">30.25</td>
    <td align="right">25.08</td>
    <td align="right">17.62</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">25.46</td>
    <td align="right">23.74</td>
    <td align="right">17.18</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">31.69</td>
    <td align="right">24.30</td>
    <td align="right">19.98</td>
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
    <td align="right">34.75</td>
    <td align="right">8.02</td>
    <td align="right">3.49</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1635</td>
    <td align="right">12.01</td>
    <td align="right">10.73</td>
    <td align="right">16.37</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.81</td>
    <td align="right">5.18</td>
    <td align="right">10.11</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.95</td>
    <td align="right">6.09</td>
    <td align="right">12.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.20</td>
    <td align="right">15.79</td>
    <td align="right">16.94</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.90</td>
    <td align="right">6.01</td>
    <td align="right">9.29</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.01</td>
    <td align="right">7.02</td>
    <td align="right">11.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.43</td>
    <td align="right">18.74</td>
    <td align="right">16.12</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.59</td>
    <td align="right">7.57</td>
    <td align="right">10.72</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.30</td>
    <td align="right">8.45</td>
    <td align="right">10.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.19</td>
    <td align="right">23.66</td>
    <td align="right">16.54</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.89</td>
    <td align="right">9.21</td>
    <td align="right">10.90</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.36</td>
    <td align="right">9.18</td>
    <td align="right">10.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4274</td>
    <td align="right">7.88</td>
    <td align="right">5.52</td>
    <td align="right">5.62</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.12</td>
    <td align="right">5.53</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.36</td>
    <td align="right">3.88</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.14</td>
    <td align="right">8.21</td>
    <td align="right">8.13</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.97</td>
    <td align="right">7.81</td>
    <td align="right">8.69</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.87</td>
    <td align="right">4.90</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.36</td>
    <td align="right">10.68</td>
    <td align="right">10.70</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.91</td>
    <td align="right">10.71</td>
    <td align="right">10.45</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.95</td>
    <td align="right">7.05</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.12</td>
    <td align="right">14.16</td>
    <td align="right">14.11</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.92</td>
    <td align="right">12.64</td>
    <td align="right">13.63</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.03</td>
    <td align="right">7.11</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4803</td>
    <td align="right">3.34</td>
    <td align="right">3.82</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.47</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.64</td>
    <td align="right">5.40</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.26</td>
    <td align="right">5.49</td>
    <td align="right">4.67</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.72</td>
    <td align="right">5.79</td>
    <td align="right">5.01</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.96</td>
    <td align="right">7.08</td>
    <td align="right">6.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.04</td>
    <td align="right">6.75</td>
    <td align="right">5.00</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.78</td>
    <td align="right">9.13</td>
    <td align="right">7.41</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.86</td>
    <td align="right">9.20</td>
    <td align="right">7.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.15</td>
    <td align="right">6.85</td>
    <td align="right">5.04</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.25</td>
    <td align="right">10.66</td>
    <td align="right">7.69</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.17</td>
    <td align="right">10.66</td>
    <td align="right">7.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">8.49</td>
    <td align="right">8.34</td>
    <td align="right">15.45</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.90</td>
    <td align="right">8.07</td>
    <td align="right">14.95</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.93</td>
    <td align="right">11.23</td>
    <td align="right">19.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.68</td>
    <td align="right">10.65</td>
    <td align="right">15.66</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.99</td>
    <td align="right">10.84</td>
    <td align="right">16.15</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.88</td>
    <td align="right">13.27</td>
    <td align="right">17.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.13</td>
    <td align="right">13.67</td>
    <td align="right">17.03</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.35</td>
    <td align="right">13.15</td>
    <td align="right">17.02</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.45</td>
    <td align="right">17.50</td>
    <td align="right">20.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">18.51</td>
    <td align="right">16.58</td>
    <td align="right">20.86</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.29</td>
    <td align="right">16.81</td>
    <td align="right">20.78</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.13</td>
    <td align="right">20.70</td>
    <td align="right">22.71</td>
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
    <td align="right">39.60</td>
    <td align="right">19.86</td>
    <td align="right">7.05</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1566</td>
    <td align="right">14.37</td>
    <td align="right">11.42</td>
    <td align="right">16.97</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.01</td>
    <td align="right">5.98</td>
    <td align="right">10.45</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.93</td>
    <td align="right">7.17</td>
    <td align="right">12.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.03</td>
    <td align="right">17.10</td>
    <td align="right">17.69</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.55</td>
    <td align="right">7.11</td>
    <td align="right">9.70</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.19</td>
    <td align="right">8.18</td>
    <td align="right">11.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.47</td>
    <td align="right">20.97</td>
    <td align="right">16.77</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.22</td>
    <td align="right">8.76</td>
    <td align="right">11.60</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.78</td>
    <td align="right">9.91</td>
    <td align="right">11.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">49.38</td>
    <td align="right">43.75</td>
    <td align="right">18.84</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.00</td>
    <td align="right">11.69</td>
    <td align="right">12.75</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.27</td>
    <td align="right">12.16</td>
    <td align="right">12.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4515</td>
    <td align="right">9.30</td>
    <td align="right">6.20</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.50</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.69</td>
    <td align="right">4.17</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.39</td>
    <td align="right">9.74</td>
    <td align="right">9.73</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.41</td>
    <td align="right">8.54</td>
    <td align="right">9.24</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.18</td>
    <td align="right">5.33</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.33</td>
    <td align="right">12.43</td>
    <td align="right">12.49</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.48</td>
    <td align="right">11.78</td>
    <td align="right">11.48</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.64</td>
    <td align="right">7.78</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">22.04</td>
    <td align="right">19.12</td>
    <td align="right">18.70</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.67</td>
    <td align="right">15.81</td>
    <td align="right">16.70</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">6.99</td>
    <td align="right">8.94</td>
    <td align="right">7.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4625</td>
    <td align="right">3.76</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.89</td>
    <td align="right">5.85</td>
    <td align="right">5.86</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.14</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.60</td>
    <td align="right">5.98</td>
    <td align="right">5.03</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.22</td>
    <td align="right">6.23</td>
    <td align="right">5.38</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.64</td>
    <td align="right">7.61</td>
    <td align="right">6.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.32</td>
    <td align="right">8.01</td>
    <td align="right">6.02</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.69</td>
    <td align="right">9.97</td>
    <td align="right">8.16</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.00</td>
    <td align="right">10.49</td>
    <td align="right">8.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.99</td>
    <td align="right">9.72</td>
    <td align="right">7.37</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.33</td>
    <td align="right">13.41</td>
    <td align="right">9.66</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.18</td>
    <td align="right">13.53</td>
    <td align="right">10.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">9.64</td>
    <td align="right">9.14</td>
    <td align="right">15.89</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.96</td>
    <td align="right">8.93</td>
    <td align="right">15.40</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.57</td>
    <td align="right">11.98</td>
    <td align="right">20.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.56</td>
    <td align="right">11.83</td>
    <td align="right">16.36</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.73</td>
    <td align="right">12.21</td>
    <td align="right">16.83</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.91</td>
    <td align="right">14.31</td>
    <td align="right">18.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.09</td>
    <td align="right">15.52</td>
    <td align="right">18.25</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">15.95</td>
    <td align="right">14.74</td>
    <td align="right">17.83</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">20.13</td>
    <td align="right">19.15</td>
    <td align="right">21.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.73</td>
    <td align="right">20.79</td>
    <td align="right">24.51</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.82</td>
    <td align="right">21.10</td>
    <td align="right">24.61</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.89</td>
    <td align="right">26.34</td>
    <td align="right">26.73</td>
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
    <td align="right">62.19</td>
    <td align="right">32.54</td>
    <td align="right">17.85</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1546</td>
    <td align="right">27.17</td>
    <td align="right">38.82</td>
    <td align="right">34.22</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.53</td>
    <td align="right">18.90</td>
    <td align="right">20.01</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.06</td>
    <td align="right">20.44</td>
    <td align="right">22.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.90</td>
    <td align="right">59.65</td>
    <td align="right">36.33</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.28</td>
    <td align="right">20.35</td>
    <td align="right">18.80</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">15.74</td>
    <td align="right">22.48</td>
    <td align="right">21.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.94</td>
    <td align="right">73.32</td>
    <td align="right">35.70</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.39</td>
    <td align="right">22.70</td>
    <td align="right">18.32</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.15</td>
    <td align="right">25.14</td>
    <td align="right">19.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.82</td>
    <td align="right">96.32</td>
    <td align="right">36.61</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.09</td>
    <td align="right">25.14</td>
    <td align="right">17.84</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.93</td>
    <td align="right">25.71</td>
    <td align="right">19.21</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4144</td>
    <td align="right">16.18</td>
    <td align="right">21.24</td>
    <td align="right">21.22</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.38</td>
    <td align="right">22.21</td>
    <td align="right">22.15</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">11.03</td>
    <td align="right">13.55</td>
    <td align="right">13.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">20.86</td>
    <td align="right">25.93</td>
    <td align="right">25.90</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.37</td>
    <td align="right">27.67</td>
    <td align="right">27.70</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.01</td>
    <td align="right">15.78</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.80</td>
    <td align="right">33.20</td>
    <td align="right">33.38</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.53</td>
    <td align="right">46.69</td>
    <td align="right">46.41</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.01</td>
    <td align="right">19.36</td>
    <td align="right">19.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.46</td>
    <td align="right">35.94</td>
    <td align="right">35.95</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.54</td>
    <td align="right">56.55</td>
    <td align="right">56.25</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.31</td>
    <td align="right">25.65</td>
    <td align="right">25.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4627</td>
    <td align="right">15.44</td>
    <td align="right">15.59</td>
    <td align="right">15.56</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.18</td>
    <td align="right">21.23</td>
    <td align="right">21.23</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.45</td>
    <td align="right">22.17</td>
    <td align="right">22.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.03</td>
    <td align="right">20.38</td>
    <td align="right">20.36</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.00</td>
    <td align="right">25.90</td>
    <td align="right">25.85</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.44</td>
    <td align="right">27.74</td>
    <td align="right">27.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.36</td>
    <td align="right">24.61</td>
    <td align="right">24.63</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.89</td>
    <td align="right">33.20</td>
    <td align="right">33.44</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.62</td>
    <td align="right">46.86</td>
    <td align="right">46.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.00</td>
    <td align="right">37.04</td>
    <td align="right">36.92</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.45</td>
    <td align="right">35.87</td>
    <td align="right">35.86</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.36</td>
    <td align="right">56.40</td>
    <td align="right">56.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">12.86</td>
    <td align="right">16.14</td>
    <td align="right">23.91</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.13</td>
    <td align="right">20.62</td>
    <td align="right">25.33</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.16</td>
    <td align="right">28.95</td>
    <td align="right">34.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.59</td>
    <td align="right">22.61</td>
    <td align="right">24.82</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.51</td>
    <td align="right">28.23</td>
    <td align="right">26.70</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.32</td>
    <td align="right">33.88</td>
    <td align="right">30.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.72</td>
    <td align="right">26.52</td>
    <td align="right">24.04</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.58</td>
    <td align="right">35.62</td>
    <td align="right">26.37</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.78</td>
    <td align="right">41.54</td>
    <td align="right">32.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">27.45</td>
    <td align="right">28.18</td>
    <td align="right">25.11</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.39</td>
    <td align="right">40.98</td>
    <td align="right">27.38</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.68</td>
    <td align="right">44.34</td>
    <td align="right">31.74</td>
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
    <td align="right">87.12</td>
    <td align="right">111.32</td>
    <td align="right">22.79</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1489</td>
    <td align="right">28.12</td>
    <td align="right">40.50</td>
    <td align="right">39.43</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.03</td>
    <td align="right">19.08</td>
    <td align="right">21.14</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.66</td>
    <td align="right">20.56</td>
    <td align="right">24.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">39.40</td>
    <td align="right">66.28</td>
    <td align="right">39.29</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">20.13</td>
    <td align="right">23.51</td>
    <td align="right">21.06</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">17.95</td>
    <td align="right">26.44</td>
    <td align="right">25.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">56.26</td>
    <td align="right">94.80</td>
    <td align="right">49.82</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">23.02</td>
    <td align="right">31.44</td>
    <td align="right">27.89</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">27.41</td>
    <td align="right">38.68</td>
    <td align="right">33.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">191.95</td>
    <td align="right">212.08</td>
    <td align="right">65.36</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">37.50</td>
    <td align="right">43.05</td>
    <td align="right">31.60</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">48.27</td>
    <td align="right">71.19</td>
    <td align="right">36.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4525</td>
    <td align="right">17.04</td>
    <td align="right">22.51</td>
    <td align="right">22.42</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">34.69</td>
    <td align="right">25.24</td>
    <td align="right">24.76</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.34</td>
    <td align="right">14.07</td>
    <td align="right">14.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.26</td>
    <td align="right">31.04</td>
    <td align="right">30.95</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">63.06</td>
    <td align="right">34.68</td>
    <td align="right">35.25</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">16.43</td>
    <td align="right">19.27</td>
    <td align="right">17.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">63.25</td>
    <td align="right">76.63</td>
    <td align="right">72.63</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">82.59</td>
    <td align="right">79.09</td>
    <td align="right">70.98</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">22.94</td>
    <td align="right">36.92</td>
    <td align="right">37.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">65.61</td>
    <td align="right">74.61</td>
    <td align="right">77.08</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">109.36</td>
    <td align="right">93.60</td>
    <td align="right">91.45</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">52.94</td>
    <td align="right">63.06</td>
    <td align="right">70.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4723</td>
    <td align="right">16.44</td>
    <td align="right">16.16</td>
    <td align="right">16.78</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">18.66</td>
    <td align="right">22.04</td>
    <td align="right">22.03</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">38.60</td>
    <td align="right">23.86</td>
    <td align="right">24.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">25.91</td>
    <td align="right">26.51</td>
    <td align="right">26.50</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.14</td>
    <td align="right">33.07</td>
    <td align="right">31.86</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">58.10</td>
    <td align="right">39.61</td>
    <td align="right">45.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.87</td>
    <td align="right">44.46</td>
    <td align="right">45.94</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">55.29</td>
    <td align="right">56.16</td>
    <td align="right">64.39</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">83.07</td>
    <td align="right">84.84</td>
    <td align="right">55.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">81.94</td>
    <td align="right">88.00</td>
    <td align="right">87.64</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">60.40</td>
    <td align="right">70.67</td>
    <td align="right">68.56</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">101.65</td>
    <td align="right">88.39</td>
    <td align="right">81.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">13.01</td>
    <td align="right">16.48</td>
    <td align="right">25.13</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.51</td>
    <td align="right">21.56</td>
    <td align="right">26.33</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">33.56</td>
    <td align="right">30.19</td>
    <td align="right">36.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">22.78</td>
    <td align="right">25.76</td>
    <td align="right">27.16</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">30.27</td>
    <td align="right">36.33</td>
    <td align="right">30.66</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">54.12</td>
    <td align="right">43.36</td>
    <td align="right">37.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">32.91</td>
    <td align="right">39.10</td>
    <td align="right">33.11</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">45.90</td>
    <td align="right">53.40</td>
    <td align="right">34.15</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">83.22</td>
    <td align="right">83.11</td>
    <td align="right">49.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">52.39</td>
    <td align="right">55.73</td>
    <td align="right">38.39</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">66.15</td>
    <td align="right">73.73</td>
    <td align="right">43.36</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">113.08</td>
    <td align="right">96.61</td>
    <td align="right">59.89</td>
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
    <td align="right">65.08</td>
    <td align="right">11.05</td>
    <td align="right">7.94</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1546</td>
    <td align="right">14.42</td>
    <td align="right">23.14</td>
    <td align="right">26.98</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.63</td>
    <td align="right">13.00</td>
    <td align="right">13.12</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">12.01</td>
    <td align="right">16.64</td>
    <td align="right">16.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.65</td>
    <td align="right">35.59</td>
    <td align="right">29.23</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.31</td>
    <td align="right">17.25</td>
    <td align="right">17.62</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.75</td>
    <td align="right">20.31</td>
    <td align="right">20.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.29</td>
    <td align="right">47.55</td>
    <td align="right">30.17</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.83</td>
    <td align="right">20.56</td>
    <td align="right">20.46</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.81</td>
    <td align="right">22.59</td>
    <td align="right">22.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">33.05</td>
    <td align="right">60.81</td>
    <td align="right">30.48</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.72</td>
    <td align="right">22.41</td>
    <td align="right">22.47</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.21</td>
    <td align="right">29.63</td>
    <td align="right">29.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4144</td>
    <td align="right">12.94</td>
    <td align="right">16.22</td>
    <td align="right">16.26</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.37</td>
    <td align="right">16.82</td>
    <td align="right">16.78</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.20</td>
    <td align="right">9.46</td>
    <td align="right">9.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.54</td>
    <td align="right">22.54</td>
    <td align="right">22.62</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.54</td>
    <td align="right">22.47</td>
    <td align="right">22.42</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.93</td>
    <td align="right">14.02</td>
    <td align="right">14.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.23</td>
    <td align="right">32.39</td>
    <td align="right">32.44</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">26.01</td>
    <td align="right">30.90</td>
    <td align="right">30.91</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.69</td>
    <td align="right">17.66</td>
    <td align="right">17.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.50</td>
    <td align="right">35.95</td>
    <td align="right">34.77</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.14</td>
    <td align="right">36.21</td>
    <td align="right">36.41</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.44</td>
    <td align="right">20.59</td>
    <td align="right">20.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4627</td>
    <td align="right">7.40</td>
    <td align="right">9.40</td>
    <td align="right">9.43</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.73</td>
    <td align="right">16.19</td>
    <td align="right">16.42</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.32</td>
    <td align="right">16.80</td>
    <td align="right">16.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.70</td>
    <td align="right">13.78</td>
    <td align="right">13.74</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.50</td>
    <td align="right">22.46</td>
    <td align="right">22.54</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.41</td>
    <td align="right">22.34</td>
    <td align="right">22.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.79</td>
    <td align="right">17.71</td>
    <td align="right">17.72</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.15</td>
    <td align="right">32.31</td>
    <td align="right">32.34</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.88</td>
    <td align="right">30.77</td>
    <td align="right">30.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.10</td>
    <td align="right">20.91</td>
    <td align="right">20.78</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.32</td>
    <td align="right">35.97</td>
    <td align="right">36.05</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.13</td>
    <td align="right">36.05</td>
    <td align="right">36.06</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">9.87</td>
    <td align="right">11.23</td>
    <td align="right">19.45</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.45</td>
    <td align="right">16.49</td>
    <td align="right">19.98</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.71</td>
    <td align="right">33.23</td>
    <td align="right">36.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">14.81</td>
    <td align="right">16.36</td>
    <td align="right">19.45</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.49</td>
    <td align="right">23.45</td>
    <td align="right">21.42</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.59</td>
    <td align="right">37.81</td>
    <td align="right">35.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">17.94</td>
    <td align="right">19.80</td>
    <td align="right">22.89</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.09</td>
    <td align="right">28.89</td>
    <td align="right">24.20</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.27</td>
    <td align="right">43.29</td>
    <td align="right">38.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">20.41</td>
    <td align="right">22.76</td>
    <td align="right">24.89</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.13</td>
    <td align="right">36.93</td>
    <td align="right">28.24</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">66.05</td>
    <td align="right">49.23</td>
    <td align="right">41.71</td>
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
    <td align="right">81.41</td>
    <td align="right">52.88</td>
    <td align="right">10.86</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1489</td>
    <td align="right">14.55</td>
    <td align="right">23.49</td>
    <td align="right">29.07</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.96</td>
    <td align="right">13.36</td>
    <td align="right">13.35</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.20</td>
    <td align="right">18.00</td>
    <td align="right">17.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.50</td>
    <td align="right">34.99</td>
    <td align="right">30.00</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.20</td>
    <td align="right">17.68</td>
    <td align="right">21.55</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.50</td>
    <td align="right">20.10</td>
    <td align="right">20.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">25.73</td>
    <td align="right">50.40</td>
    <td align="right">31.17</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">20.70</td>
    <td align="right">27.53</td>
    <td align="right">21.62</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">16.77</td>
    <td align="right">22.69</td>
    <td align="right">29.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">31.80</td>
    <td align="right">71.32</td>
    <td align="right">40.27</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">15.05</td>
    <td align="right">24.88</td>
    <td align="right">28.18</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">21.56</td>
    <td align="right">42.26</td>
    <td align="right">47.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4525</td>
    <td align="right">13.24</td>
    <td align="right">17.14</td>
    <td align="right">17.22</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.66</td>
    <td align="right">18.08</td>
    <td align="right">18.02</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.46</td>
    <td align="right">9.83</td>
    <td align="right">9.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.32</td>
    <td align="right">22.08</td>
    <td align="right">22.64</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.51</td>
    <td align="right">22.58</td>
    <td align="right">22.35</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.14</td>
    <td align="right">14.34</td>
    <td align="right">14.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.22</td>
    <td align="right">33.21</td>
    <td align="right">37.08</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">28.57</td>
    <td align="right">34.10</td>
    <td align="right">39.88</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">31.27</td>
    <td align="right">57.86</td>
    <td align="right">20.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">27.98</td>
    <td align="right">48.27</td>
    <td align="right">44.89</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">55.02</td>
    <td align="right">44.27</td>
    <td align="right">43.91</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">21.01</td>
    <td align="right">28.53</td>
    <td align="right">32.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4723</td>
    <td align="right">6.94</td>
    <td align="right">10.10</td>
    <td align="right">9.90</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.63</td>
    <td align="right">17.23</td>
    <td align="right">17.32</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.67</td>
    <td align="right">18.13</td>
    <td align="right">18.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.22</td>
    <td align="right">14.42</td>
    <td align="right">13.99</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.12</td>
    <td align="right">21.96</td>
    <td align="right">22.06</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.55</td>
    <td align="right">22.62</td>
    <td align="right">22.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">12.84</td>
    <td align="right">18.19</td>
    <td align="right">19.68</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">27.08</td>
    <td align="right">38.46</td>
    <td align="right">34.44</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">30.86</td>
    <td align="right">37.63</td>
    <td align="right">45.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">24.78</td>
    <td align="right">27.09</td>
    <td align="right">22.54</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">30.04</td>
    <td align="right">39.50</td>
    <td align="right">39.18</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">37.49</td>
    <td align="right">39.36</td>
    <td align="right">39.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">11.63</td>
    <td align="right">11.52</td>
    <td align="right">19.84</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.74</td>
    <td align="right">17.22</td>
    <td align="right">20.68</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">50.90</td>
    <td align="right">34.02</td>
    <td align="right">38.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">15.68</td>
    <td align="right">16.96</td>
    <td align="right">19.44</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">20.35</td>
    <td align="right">24.60</td>
    <td align="right">21.05</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">59.66</td>
    <td align="right">38.44</td>
    <td align="right">40.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">19.98</td>
    <td align="right">20.85</td>
    <td align="right">24.30</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.14</td>
    <td align="right">30.06</td>
    <td align="right">25.21</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">69.20</td>
    <td align="right">50.69</td>
    <td align="right">43.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">22.74</td>
    <td align="right">24.97</td>
    <td align="right">29.25</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">34.96</td>
    <td align="right">44.33</td>
    <td align="right">30.88</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">80.50</td>
    <td align="right">58.73</td>
    <td align="right">45.02</td>
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
    <td align="right">43.70</td>
    <td align="right">8.97</td>
    <td align="right">7.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1546</td>
    <td align="right">59.39</td>
    <td align="right">58.38</td>
    <td align="right">42.07</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">22.13</td>
    <td align="right">38.59</td>
    <td align="right">34.84</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">24.96</td>
    <td align="right">42.49</td>
    <td align="right">37.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.36</td>
    <td align="right">83.82</td>
    <td align="right">44.27</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.91</td>
    <td align="right">42.65</td>
    <td align="right">34.53</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.18</td>
    <td align="right">48.09</td>
    <td align="right">37.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">109.91</td>
    <td align="right">101.06</td>
    <td align="right">43.58</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.00</td>
    <td align="right">48.09</td>
    <td align="right">34.58</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.41</td>
    <td align="right">52.91</td>
    <td align="right">37.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.79</td>
    <td align="right">125.64</td>
    <td align="right">44.43</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.25</td>
    <td align="right">53.62</td>
    <td align="right">35.13</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.00</td>
    <td align="right">57.82</td>
    <td align="right">36.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4144</td>
    <td align="right">24.43</td>
    <td align="right">42.60</td>
    <td align="right">42.61</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">26.79</td>
    <td align="right">42.97</td>
    <td align="right">43.26</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.68</td>
    <td align="right">24.98</td>
    <td align="right">24.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.14</td>
    <td align="right">58.23</td>
    <td align="right">58.85</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.24</td>
    <td align="right">60.89</td>
    <td align="right">59.13</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.49</td>
    <td align="right">36.18</td>
    <td align="right">25.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">39.94</td>
    <td align="right">79.80</td>
    <td align="right">80.34</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.40</td>
    <td align="right">80.74</td>
    <td align="right">80.59</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.81</td>
    <td align="right">54.79</td>
    <td align="right">39.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.40</td>
    <td align="right">89.14</td>
    <td align="right">88.45</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">50.98</td>
    <td align="right">94.66</td>
    <td align="right">94.60</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.20</td>
    <td align="right">55.88</td>
    <td align="right">40.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4823</td>
    <td align="right">18.65</td>
    <td align="right">26.15</td>
    <td align="right">26.19</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.64</td>
    <td align="right">28.98</td>
    <td align="right">29.12</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.85</td>
    <td align="right">30.98</td>
    <td align="right">31.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.91</td>
    <td align="right">46.84</td>
    <td align="right">34.81</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.55</td>
    <td align="right">41.91</td>
    <td align="right">27.47</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">20.96</td>
    <td align="right">51.68</td>
    <td align="right">40.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.69</td>
    <td align="right">54.38</td>
    <td align="right">39.07</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.98</td>
    <td align="right">52.80</td>
    <td align="right">35.07</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.30</td>
    <td align="right">60.98</td>
    <td align="right">43.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.82</td>
    <td align="right">55.19</td>
    <td align="right">39.36</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.65</td>
    <td align="right">64.09</td>
    <td align="right">43.88</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.31</td>
    <td align="right">63.75</td>
    <td align="right">44.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">23.66</td>
    <td align="right">24.18</td>
    <td align="right">32.45</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.34</td>
    <td align="right">44.34</td>
    <td align="right">37.90</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.93</td>
    <td align="right">50.92</td>
    <td align="right">44.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.12</td>
    <td align="right">33.84</td>
    <td align="right">38.64</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">36.02</td>
    <td align="right">60.35</td>
    <td align="right">43.97</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.73</td>
    <td align="right">63.24</td>
    <td align="right">48.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">37.63</td>
    <td align="right">38.28</td>
    <td align="right">40.92</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.78</td>
    <td align="right">73.01</td>
    <td align="right">44.22</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.19</td>
    <td align="right">80.03</td>
    <td align="right">52.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">46.33</td>
    <td align="right">47.32</td>
    <td align="right">49.84</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">51.48</td>
    <td align="right">94.40</td>
    <td align="right">55.04</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.52</td>
    <td align="right">99.27</td>
    <td align="right">59.56</td>
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
    <td align="right">67.62</td>
    <td align="right">36.77</td>
    <td align="right">12.41</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">2.1489</td>
    <td align="right">68.24</td>
    <td align="right">65.08</td>
    <td align="right">47.29</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">24.11</td>
    <td align="right">40.95</td>
    <td align="right">38.53</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.17</td>
    <td align="right">44.69</td>
    <td align="right">42.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">101.94</td>
    <td align="right">91.48</td>
    <td align="right">49.40</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">28.79</td>
    <td align="right">47.12</td>
    <td align="right">40.47</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">33.48</td>
    <td align="right">58.36</td>
    <td align="right">45.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">149.53</td>
    <td align="right">127.05</td>
    <td align="right">50.89</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">52.64</td>
    <td align="right">66.42</td>
    <td align="right">44.95</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">47.86</td>
    <td align="right">73.87</td>
    <td align="right">57.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">263.84</td>
    <td align="right">210.04</td>
    <td align="right">62.97</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">53.26</td>
    <td align="right">80.36</td>
    <td align="right">52.90</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">61.36</td>
    <td align="right">85.38</td>
    <td align="right">67.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.4525</td>
    <td align="right">27.61</td>
    <td align="right">51.18</td>
    <td align="right">44.63</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.16</td>
    <td align="right">49.80</td>
    <td align="right">52.51</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.98</td>
    <td align="right">31.52</td>
    <td align="right">35.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.25</td>
    <td align="right">66.64</td>
    <td align="right">68.46</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">46.92</td>
    <td align="right">79.98</td>
    <td align="right">72.53</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">21.79</td>
    <td align="right">46.22</td>
    <td align="right">34.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.45</td>
    <td align="right">86.13</td>
    <td align="right">87.07</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">68.90</td>
    <td align="right">108.96</td>
    <td align="right">98.88</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">82.85</td>
    <td align="right">111.99</td>
    <td align="right">87.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">63.79</td>
    <td align="right">118.61</td>
    <td align="right">113.70</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.26</td>
    <td align="right">127.75</td>
    <td align="right">128.84</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">76.51</td>
    <td align="right">124.24</td>
    <td align="right">101.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.4632</td>
    <td align="right">20.69</td>
    <td align="right">33.60</td>
    <td align="right">32.32</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">23.09</td>
    <td align="right">36.35</td>
    <td align="right">37.31</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">23.31</td>
    <td align="right">38.97</td>
    <td align="right">40.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">23.93</td>
    <td align="right">69.88</td>
    <td align="right">50.27</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">20.89</td>
    <td align="right">55.84</td>
    <td align="right">40.92</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">30.00</td>
    <td align="right">81.22</td>
    <td align="right">64.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">54.36</td>
    <td align="right">103.11</td>
    <td align="right">87.01</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">50.24</td>
    <td align="right">72.67</td>
    <td align="right">52.13</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">58.30</td>
    <td align="right">79.80</td>
    <td align="right">57.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">75.13</td>
    <td align="right">117.17</td>
    <td align="right">96.27</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">51.94</td>
    <td align="right">94.85</td>
    <td align="right">65.36</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">47.61</td>
    <td align="right">93.18</td>
    <td align="right">71.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">26.31</td>
    <td align="right">26.49</td>
    <td align="right">36.87</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.94</td>
    <td align="right">47.88</td>
    <td align="right">44.24</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">38.58</td>
    <td align="right">56.71</td>
    <td align="right">57.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">42.92</td>
    <td align="right">43.36</td>
    <td align="right">50.40</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">51.54</td>
    <td align="right">84.29</td>
    <td align="right">61.98</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">74.44</td>
    <td align="right">98.77</td>
    <td align="right">83.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">67.61</td>
    <td align="right">91.31</td>
    <td align="right">80.18</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">66.98</td>
    <td align="right">96.55</td>
    <td align="right">72.77</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">89.31</td>
    <td align="right">122.28</td>
    <td align="right">118.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">84.49</td>
    <td align="right">89.73</td>
    <td align="right">94.89</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">92.54</td>
    <td align="right">137.63</td>
    <td align="right">101.76</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">130.95</td>
    <td align="right">165.94</td>
    <td align="right">120.35</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
